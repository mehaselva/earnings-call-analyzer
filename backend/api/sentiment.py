from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
from dotenv import load_dotenv
import os

load_dotenv()


def analyze_sentiment(text):
    prompt = f"Label the sentiment of this executive response as bullish, neutral, or bearish:\n\n{text}"
    response = client.chat.completions.create(model="gpt-4",
    messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content.strip()
