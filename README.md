# PDF to Markdown Converter

A simple Python + Streamlit app to upload a PDF, send it to LlamaParse / LlamaCloud, and return Markdown.

## Features

- Upload PDF files
- Convert PDF content to Markdown
- Preview Markdown in the browser
- Download output as `.md`
- Keeps API keys out of source control

## Tech Stack

- Python
- Streamlit
- LlamaParse / LlamaCloud
- python-dotenv

## Setup

Clone the repo:

    git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
    cd YOUR_REPO_NAME

Create and activate a virtual environment:

    python -m venv .venv

macOS / Linux:

    source .venv/bin/activate

Windows PowerShell:

    .venv\Scripts\Activate.ps1

Install dependencies:

    pip install -r requirements.txt

## Environment Variables

Create a `.env` file from the example:

    cp .env.example .env

Add your LlamaCloud API key:

    LLAMA_CLOUD_API_KEY=your_llama_cloud_api_key_here

Do not commit `.env` to GitHub.

## Run

    streamlit run app.py

Open the local URL shown in the terminal, usually:

    http://localhost:8501

## Usage

1. Upload a PDF.
2. Click **Convert to Markdown**.
3. Preview the Markdown.
4. Download the `.md` file.

## GitHub Notes

Commit `.env.example`, not `.env`.

Recommended `.gitignore` entries:

    .env
    .venv/
    __pycache__/
    *.py[cod]
    .streamlit/secrets.toml

## Security Note

Uploaded PDFs are sent to a third-party parsing API. Do not upload sensitive documents unless you are comfortable with that provider’s terms and data handling.
