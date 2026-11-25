
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path
import ollama

app = FastAPI(title="Local AI Assistant API")

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_DIR),
    name="static"
)

MODEL = "llama3.2"


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]


@app.get("/")
def home():
    return FileResponse(FRONTEND_DIR / "index.html")


@app.get("/api/health")
def health():
    return {
        "status": "online",
        "model": MODEL
    }


@app.post("/api/chat")
def chat(request: ChatRequest):

    try:
        messages = [
            {
                "role": "system",
                "content": "You are a helpful AI assistant. "
                           "Give clear and friendly answers."
            }
        ]

        messages.extend([
            message.model_dump()
            for message in request.messages
        ])

        response = ollama.chat(
            model=MODEL,
            messages=messages
        )

        return {
            "response": response.message.content
        }

    except Exception as error:
        raise HTTPException(
            status_code=503,
            detail=str(error)
        )
