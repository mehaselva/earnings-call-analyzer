import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_sentiment(text):
    prompt = f"Label the sentiment of this executive response as bullish, neutral, or bearish:\n\n{text}"
    response = client.chat.completions.create(model="gpt-4o",
    messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content.strip()
