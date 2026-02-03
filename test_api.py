import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Test the API
try:
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content("Say hello in one sentence.")
    print("API Test Successful!")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"API Test Failed: {str(e)}")
