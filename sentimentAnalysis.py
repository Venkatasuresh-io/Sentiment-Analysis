import streamlit as st
from transformers import pipeline

# Load sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

st.title("Sentiment Analysis")

user_text = st.text_area("Enter a sentence:")
if user_text:
    result = sentiment_analyzer(user_text)[0]
    st.write(f"Sentiment: {result['label']} (Confidence: {result['score']:.4f})")
