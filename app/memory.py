chat_history = []

def add_history(question, answer):
    chat_history.append({"question": question, "answer": answer})

def get_history(n=3):
    return chat_history[-n:]