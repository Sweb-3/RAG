from app.retriever import retrieve_docs
from app.rerank import rerank
from app.llm import call_llm
from app.memory import get_history

def generate_answer(query):

    docs = retrieve_docs(query)
    docs = rerank(query, docs)

    context = "\n\n".join([d.page_content for d in docs])
    history = get_history()

    history_text = "\n".join(
        [f"User: {h['question']}\nAssistant: {h['answer']}" for h in history]
    )

    prompt = f"""
You are an intelligent AI assistant.

Rules:
- Answer ONLY from the provided context
- If not found, say: "I don't know from the document"
- Be clear, concise, and structured
- Use bullet points if helpful

Conversation History:
{history_text}

Context:
{context}

Question:
{query}

Answer:
"""

    return call_llm(prompt)