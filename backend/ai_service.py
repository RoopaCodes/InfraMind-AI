from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_logs(log_data):

    prompt = f"""
    You are an expert Site Reliability Engineer.

    Analyze the following infrastructure logs.

    Provide:
    1. Root Cause
    2. Severity
    3. Recommended Fix
    4. Suggested Automation

    Logs:
    {log_data}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content