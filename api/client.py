import streamlit as st
import requests

def get_ollama_response_essay(input_text):
  response = requests.post("http://localhost:8000/essay/invoke", json={"input":{ "topic": input_text}})
  return response.json()["output"]
def get_ollama_response_poem(input_text):
  response = requests.post("http://localhost:8000/poem/invoke", json={"input":{ "topic": input_text}})
  return response.json()["output"]

st.title("Chatbot")
input_text1 = st.text_input("Enter your question here:")
if input_text1:
    response = get_ollama_response_essay(input_text1)
    st.write(response)
    
## """ input_text2 = st.text_input("Enter your question here:") """
## """ if input_text2:
##     response = get_ollama_response_poem(input_text2)
##     st.write(response) """
