from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import os

from app.rag import generate_answer
from app.memory import add_history
from app.ingest import ingest_file

app = FastAPI()

class Query(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "RAG Bot Running 🚀"}

@app.post("/ask")
def ask(q: Query):
    answer = generate_answer(q.question)
    add_history(q.question, answer)
    return {"answer": answer}

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    os.makedirs("data", exist_ok=True)

    file_path = f"data/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    ingest_file(file_path)

    return {"message": "Uploaded & indexed"}