from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
from dotenv import load_dotenv
import os

load_dotenv()


def summarize_call(transcript):
    prompt = f"Summarize this earnings call transcript in 3 bullet points:\n\n{transcript}"
    response = client.chat.completions.create(model="gpt-4",
    messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content.strip()
