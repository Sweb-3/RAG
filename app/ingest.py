import os
from typing import List
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from app.config import *

def load_docs() -> List[Document]:
    docs = []

    for file in os.listdir(DATA_PATH):
        path = os.path.join(DATA_PATH, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)
        elif file.endswith(".txt"):
            loader = TextLoader(path)
        else:
            continue

        loaded_docs = loader.load()

        for doc in loaded_docs:
            doc.metadata["source"] = file

        docs.extend(loaded_docs)

    return docs


def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.split_documents(docs)


def build_db(chunks):
    embedding = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    db = FAISS.from_documents(chunks, embedding)
    os.makedirs(DB_PATH, exist_ok=True)
    db.save_local(DB_PATH)


def run_ingest():
    docs = load_docs()
    chunks = split_docs(docs)
    build_db(chunks)