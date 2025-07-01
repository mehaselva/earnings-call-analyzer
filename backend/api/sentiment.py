import openai

def analyze_sentiment(text):
    prompt = f"Label the sentiment of this executive response as bullish, neutral, or bearish:\n\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
