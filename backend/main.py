from fastapi import FastAPI, UploadFile
from api.transcribe import transcribe_audio
from api.summarizer import summarize_call
from api.sentiment import analyze_sentiment
import tempfile

app = FastAPI()

@app.post("/analyze/")
async def analyze(file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        transcript = transcribe_audio(tmp.name)

    summary = summarize_call(transcript)
    sentiment = analyze_sentiment(transcript)

    return {"transcript": transcript, "summary": summary, "sentiment": sentiment}
