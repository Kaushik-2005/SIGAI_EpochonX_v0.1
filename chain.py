from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import google.generativeai as genai
import os
from dotenv import load_dotenv

from generator.pdf import PDFGenerator
from generator.docx import DocxGenerator

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Update this line
model = GoogleGenerativeAI(model="gemini-1.5-pro")

prompt = PromptTemplate(
    prompt_template = """
    
    """
)

chain = prompt | model