# RAG Documentation Bot

## Overview
This project implements a Retrieval-Augmented Generation (RAG) system for document-based question answering.

## Features
- Document ingestion (PDF, TXT)
- Text chunking
- Vector database (FAISS)
- Semantic search
- API for querying

## Tech Stack
- Python
- LangChain
- FAISS
- HuggingFace Embeddings
- FastAPI

## How to Run

1. Add documents to `data/`
2. Run ingestion:
   python app/ingest.py
3. Start API:
   uvicorn app.main:app --reload

## Example Query
"What is this document about?"