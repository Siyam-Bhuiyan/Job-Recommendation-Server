from asyncio import run
import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
from gemini import GeminiClient
from apify_client import ApifyClient

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))



def extract_text_from_pdf(uploaded_file):
    """
    Extract text from a PDF file using PyMuPDF.
    
    Args:
        uploaded_file: The PDF file to extract text from.
        
    Returns:
        str: The extracted text from the PDF.
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def ask_gemini(prompt):
    """
    Ask a question to the Gemini model.
    
    Args:
        prompt (str): The question to ask.
        model (str): The model to use for the query.
        
    Returns:
        str: The response from the Gemini model.
    """

    response = client.chat.completions.create(
        model="GEMINI_2.0_FLASH",
        messages=[
            {
                "role": "user", 
             "content": prompt
            }
        ]
        temperature=0.5,
    )
    return response.choices[0].message.content


def fetch_linkedin_jobs(search_query, location="Bangladesh", rows=50):
    run_input = {
        "keywords": search_query,
        "maxJobs": 50,
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all",
    }

    run = apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs


# Fetch Naukri jobs based on search query and location
def fetch_naukri_jobs(search_query, location = "india", rows=60):
    run_input = {
        "keyword": search_query,
        "maxJobs": 60,
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all",
    }
    run = apify_client.actor("alpcnRV9YI9lYVPWk").call(run_input=run_input)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs