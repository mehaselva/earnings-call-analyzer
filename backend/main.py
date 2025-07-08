from fastapi import FastAPI, UploadFile
from api.transcribe import transcribe_audio
from api.summarizer import summarize_call
from api.sentiment import analyze_sentiment
import tempfile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
import traceback
from utils.youtube_fetcher import download_audio_from_youtube

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FilePathRequest(BaseModel):
    file_path: str

@app.post("/analyze-from-path/")
def analyze_from_path(request: FilePathRequest):
    try:
        transcript = transcribe_audio(request.file_path)
        summary = summarize_call(transcript)
        sentiment = analyze_sentiment(transcript)

        return {
            "summary": summary,
            "sentiment": sentiment,
            "transcript": transcript[:1000] + "..."
        }
    except Exception as e:
        print("Error in summarize-from-path:", traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Failed to summarize: {str(e)}")


@app.post("/analyze/")
async def analyze(file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        transcript = transcribe_audio(tmp.name)

    summary = summarize_call(transcript)
    sentiment = analyze_sentiment(transcript)

    return {"transcript": transcript, "summary": summary, "sentiment": sentiment}
