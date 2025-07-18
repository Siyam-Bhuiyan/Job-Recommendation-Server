# Generative AI-Powered Job Recommender System (MCP)

This project is a Generative AI-powered Job Recommendation Server built with Python. It leverages the Model Context Protocol (MCP), Gemini AI, and job APIs to provide personalized job recommendations based on user input, including PDF resume parsing.

## Features
- **Resume Parsing:** Extracts text from uploaded PDF resumes using PyMuPDF.
- **AI-Powered Recommendations:** Uses Gemini AI to analyze user input and generate job recommendations.
- **Job Aggregation:** Fetches job listings from LinkedIn and Naukri using the Apify API.
- **Environment Variables:** Securely manages API keys and tokens using a `.env` file.

## Tech Stack
- Python 3.8+
- Streamlit (for UI, if used)
- PyMuPDF (fitz)
- Gemini AI (Google)
- Apify Client
- python-dotenv

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Siyam-Bhuiyan/Job-Recommendation-Server.git
cd Job-Recommendation-Server
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the project root with the following content:
```env
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
PYMUPDF_API_KEY=your_pymupdf_api_key
APIFY_API_TOKEN=your_apify_api_token
```


