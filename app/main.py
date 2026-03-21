from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import os
import shutil

from app.rag import generate_answer
from app.ingest import run_ingest
from app.config import DATA_PATH

app = FastAPI(title="RAG Documentation Bot")

class Query(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "RAG Bot is running 🚀"}

# 🔍 Ask
@app.post("/ask")
def ask(q: Query):
    result = generate_answer(q.question)
    return {"question": q.question, "answer": result}

# 📂 Upload + Auto Index
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    os.makedirs(DATA_PATH, exist_ok=True)

    file_path = os.path.join(DATA_PATH, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 🔥 auto ingest
    run_ingest()

    return {"message": f"{file.filename} uploaded & indexed"}