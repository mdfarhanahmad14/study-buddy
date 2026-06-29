import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="AI Study Buddy", page_icon="📚")
st.title("📚 AI-Powered Study Buddy")

tab1, tab2, tab3 = st.tabs(["🧠 Topic Explainer", "📝 Notes Summarizer", "❓ Quiz Generator"])

with tab1:
    st.header("Topic Explainer")
    topic = st.text_input("Enter any topic you want to learn about:")
    if st.button("Explain"):
        if topic:
            with st.spinner("Understanding your topic..."):
                response = model.generate_content(f"Explain this topic in simple English for a student: {topic}")
                st.write(response.text)

with tab2:
    st.header("Notes Summarizer")
    notes = st.text_area("Paste your notes here:", height=200)
    if st.button("Summarize"):
        if notes:
            with st.spinner("Generating summary..."):
                response = model.generate_content(f"Summarize these notes in simple points: {notes}")
                st.write(response.text)

with tab3:
    st.header("Quiz Generator")
    quiz_topic = st.text_input("Enter the topic for your quiz:")
    if st.button("Generate Quiz"):
        if quiz_topic:
            with st.spinner("Generating your quiz..."):
                response = model.generate_content(f"Create 5 multiple choice questions on: {quiz_topic}. Format each as Q, options A B C D, and Answer.")
                st.write(response.text)