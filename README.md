# LegalEase-Ai
AI-Powered Legal Document Generator
LegalEase-Ai

AI-Powered Legal Document Generator

LegalEase-Ai is an AI-based web application designed to help users generate and understand legal documents in a simple and user-friendly way.

Features

- Generate legal documents from user-provided details
- Simple and easy-to-use web interface
- Preview generated documents
- Export documents in different formats
- FastAPI backend for processing requests
- Streamlit frontend for user interaction
- Easy document generation workflow

Technologies Used

- Python
- Streamlit
- FastAPI
- HTML / CSS
- python-docx
- FPDF
- Uvicorn

Project Structure

LegalEase-Ai/
│
├── backend/
│   ├── main.py
│   ├── routes/
│   └── services/
│
├── frondend/
│   └── app.py
│
├── .gitignore
├── requirements.txt
└── README.md

Installation

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/LegalEase-Ai.git

2. Open the project

cd LegalEase-Ai

3. Create a virtual environment

python -m venv .venv

4. Activate the virtual environment

Windows PowerShell:

.\.venv\Scripts\Activate.ps1

5. Install dependencies

pip install -r requirements.txt

Running the Backend

Open a terminal and run:

uvicorn backend.main:app --reload

The FastAPI backend will normally run at:

http://127.0.0.1:8000

Running the Frontend

Open another terminal and run:

streamlit run frondend/app.py

The Streamlit application will normally open at:

http://localhost:8501

How to Use

1. Start the FastAPI backend.
2. Start the Streamlit frontend.
3. Open the Streamlit URL in your browser.
4. Enter the required legal document details.
5. Generate the document.
6. Preview or download the generated document.

Important

This project is intended for educational and document-generation purposes. It does not replace professional legal advice.

Future Improvements

- Add more legal document templates
- Add multilingual support
- Improve document formatting
- Add user authentication
- Add cloud deployment
- Add database support
- Improve AI-based document assistance

Author

Aravindh

License

This project is for educational purposes.