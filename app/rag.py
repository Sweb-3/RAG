from app.retriever import retrieve_docs

def generate_answer(query: str):
    docs = retrieve_docs(query)

    if not docs:
        return "No relevant documents found."

    context = "\n\n".join([doc.page_content for doc in docs])

    return f"🔍 Retrieved Context:\n{context[:1000]}"