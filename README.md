# Job Recommendation Service (MCP)
# Generative AI-Based

This project is a Generative AI-powered Job Recommendation Server built with Python; leverages the MCP, Gemini, and job APIs to provide personalized job recommendations based on user input, including CV,PDF resume parsing.


## Tech Stack
- Python 3.8+
- Streamlit 
- PyMuPDF (fitz)
- Gemini AI (Google)
- Apify Client


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
OPENAI_API_KEY=your_openai_api_key or
GEMINI_API_KEY=your_gemini_api_key
PYMUPDF_API_KEY=your_pymupdf_api_key
APIFY_API_TOKEN=your_apify_api_token
```


