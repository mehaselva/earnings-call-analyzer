import openai

def summarize_call(transcript):
    prompt = f"Summarize this earnings call transcript in 3 bullet points:\n\n{transcript}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
