from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
import fitz  # PyMuPDF for PDF
import docx  # For DOCX files
import requests
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
HF_API_URL = "https://api-inference.huggingface.co/models/google/pegasus-xsum"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def query_hf_api(payload):
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
    response = requests.post(HF_API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"Hugging Face API error: {response.status_code} - {response.text}")
    return response.json()

def split_text_chunks(text, max_words=700):
    words = text.split()
    return [' '.join(words[i:i + max_words]) for i in range(0, len(words), max_words)]

@app.post("/summarize-text/")
async def summarize_text(
    file: UploadFile = File(...)
):
    try:
        contents = await file.read()

        # Extract text from file type
        if file.content_type == "application/pdf":
            temp_path = f"temp_{file.filename}"
            with open(temp_path, "wb") as f:
                f.write(contents)
            doc = fitz.open(temp_path)
            text = "".join([page.get_text() for page in doc])
            doc.close()
            os.remove(temp_path)

        elif file.content_type == "text/plain":
            text = contents.decode('utf-8')

        elif file.content_type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/msword"]:
            temp_path = f"temp_{file.filename}"
            with open(temp_path, "wb") as f:
                f.write(contents)
            doc = docx.Document(temp_path)
            text = "\n".join([para.text for para in doc.paragraphs])
            os.remove(temp_path)

        else:
            return {"error": f"Unsupported file type: {file.content_type}"}

        # Clean text and split if needed
        text_chunks = split_text_chunks(text, max_words=700)

        summaries = []
        for chunk in text_chunks:
            prompt = f"Summarize the following content briefly and clearly:\n\n{chunk}"
            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_length": 150,  # ~100 words
                    "min_length": 70,
                    "do_sample": False
                },
                "options": {"wait_for_model": True}
            }
            hf_response = query_hf_api(payload)

            if isinstance(hf_response, list) and "summary_text" in hf_response[0]:
                summaries.append(hf_response[0]["summary_text"])
            else:
                # Return raw response for debugging if unexpected
                return {"error": "Unexpected response from HF API", "raw_response": hf_response}

        final_summary = "\n\n".join(summaries)
        return {"summary": final_summary or "No summary generated."}

    except Exception as e:
        print("❌ Error:", e)
        return {"error": str(e)}
