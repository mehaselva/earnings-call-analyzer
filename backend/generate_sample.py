from gtts import gTTS

sample_text = """
Good afternoon, and thank you for joining us. I'm pleased to report that in Q2, our revenue grew 18% year-over-year, driven by strong performance in the cloud infrastructure segment. 
Operating margins also improved significantly, exceeding our internal targets. Looking ahead, we anticipate continued growth momentum into Q3, especially as we expand our AI-powered offerings. 
We remain focused on disciplined investment and long-term shareholder value.
"""

tts = gTTS(sample_text)
tts.save("sample_earnings_call.mp3")

print("✅ MP3 saved as 'sample_earnings_call.mp3'")

# from openai import OpenAI
# import os
# from dotenv import load_dotenv

# load_dotenv()
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# models = client.models.list()
# for m in models.data:
#     print(m.id)
