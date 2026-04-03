from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from app.config import *

embedding = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

def ingest_file(path):
    loader = PyPDFLoader(path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(docs)

    try:
        db = FAISS.load_local(DB_PATH, embedding, allow_dangerous_deserialization=True)
        db.add_documents(chunks)
    except:
        db = FAISS.from_documents(chunks, embedding)

    db.save_local(DB_PATH)