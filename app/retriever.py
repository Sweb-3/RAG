from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from app.config import *

embedding = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

db = FAISS.load_local(DB_PATH, embedding, allow_dangerous_deserialization=True)

def retrieve_docs(query, k=5):
    return db.similarity_search(query, k=k)