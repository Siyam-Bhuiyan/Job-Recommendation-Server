from asyncio import run
import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
import google.generativeai as genai
from apify_client import ApifyClient
import google.generativeai as genai

load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel("gemini-pro")


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file.
    
    Args:
        uploaded_file (str): The path to the PDF file.
        
    Returns:
        str: The extracted text.
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text



def ask_GEMINI(prompt, max_tokens=500):
    """
    Sends a prompt to the GEMINI API and returns the response.
    
    Args:
        prompt (str): The prompt to send to the GEMINI API.
        model (str): The model to use for the request.
        temperature (float): The temperature for the response.
        
    Returns:
        str: The response from the GEMINI API.
    """
    

    response = gemini_model.generate_content(prompt)
    return response.text

