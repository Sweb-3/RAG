import streamlit as st
import requests

API = "http://api:8000"

st.title("🔥 RAG Chat Bot")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    files = {"file": uploaded_file}
    res = requests.post(f"{API}/upload", files=files)
    st.success("✅ Uploaded & Indexed!")

question = st.text_input("Ask something:")

if st.button("Send"):
    res = requests.post(f"{API}/ask", json={"question": question})
    st.write(res.json()["answer"])