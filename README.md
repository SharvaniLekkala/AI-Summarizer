cat <<EOF > README.md
# 📄 AI-Powered Document Summarizer (FastAPI + Hugging Face)

Welcome to the **AI Document Summarizer** — a smart, beginner-friendly API that lets you upload documents like PDFs, Word files, or plain text files and get a clean, readable summary in return. ✨

Whether you're a student cutting through dense notes, a developer experimenting with NLP, or someone trying to make sense of a 20-page report — this tool is for you.

>  **Note:** Currently works best for files under **1 MB** due to Hugging Face API and token limits.

---

## 🚀 What This Project Does

- ✅ Upload `.pdf`, `.docx`, or `.txt` files
- 🧠 Uses Hugging Face’s summarization model (Pegasus XSUM)
- 📚 Handles large text by breaking it into smaller chunks
- 🌐 Fully accessible via web browser (FastAPI Swagger UI)
- ⚙️ Generates ~100 word summaries (no tuning required)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| FastAPI | Web backend (Python) |
| Uvicorn | ASGI server for FastAPI |
| Hugging Face Transformers | Summarization AI |
| PyMuPDF (fitz) | For reading PDFs |
| python-docx | For reading Word files |
| python-multipart | For handling file uploads |
| dotenv | For managing API secrets securely |

---

## 📦 Setup & Installation

### 1. Clone the repository

\`\`\`bash
git clone https://github.com/your-username/document-summarizer.git
cd document-summarizer
\`\`\`

### 2. Set up a virtual environment

\`\`\`bash
python -m venv venv
\`\`\`

### 3. Activate the virtual environment

- **On Windows:**
  \`\`\`bash
  .\\venv\\Scripts\\activate
  \`\`\`

- **On macOS/Linux:**
  \`\`\`bash
  source venv/bin/activate
  \`\`\`

### 4. Install the required packages

\`\`\`bash
pip install -r requirements.txt
\`\`\`

> Or manually:
\`\`\`bash
pip install fastapi uvicorn requests python-docx pymupdf python-dotenv python-multipart
\`\`\`

---

## 🔐 Hugging Face API Setup

1. Create a free account on [huggingface.co](https://huggingface.co/)
2. Go to **Settings → Access Tokens**
3. Generate a new token (read access)
4. Create a `.env` file in your root folder:

\`\`\`.env
HUGGINGFACE_API_TOKEN=your_token_here
\`\`\`

---

## ▶️ Running the App

Start the FastAPI server with:

\`\`\`bash
uvicorn app.main:app --reload
\`\`\`

Once running, open your browser to:

\`\`\`
http://127.0.0.1:8000/docs
\`\`\`

Use the Swagger UI to upload your file and see the summary in seconds!

---

## 📁 Project Structure

\`\`\`
document-summarizer/
├── app/
│   ├── main.py
│   ├── database.py (optional)
├── venv/
├── requirements.txt
├── .env
└── README.md
\`\`\`

---

## 🧠 Who Can Use This?

- 🎓 Students summarizing lecture notes or PDFs
- 👩‍💼 Professionals breaking down large reports
- 🧑‍💻 Developers learning FastAPI + NLP
- 🧠 Anyone who wants to "TL;DR" a document quickly

---

## ⚠️ Current Limitations

- Only supports files **below 1MB**
- English text only (for now)
- Depends on internet (uses Hugging Face cloud API)

---

## 💡 Future Improvements

- Add support for scanned PDFs (OCR)
- Choose between bullet or paragraph summary styles
- Upload larger files (chunking optimization)
- Add a frontend interface

---

## 🙌 Credits

- 🤗 [Hugging Face](https://huggingface.co/) — for the AI magic
- ⚡ [FastAPI](https://fastapi.tiangolo.com/) — for the smooth backend


