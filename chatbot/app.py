from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
  [
    ("system", "You are a helpful AI assistant. Please answer the following questions."),
    ("user", "Question:{question}"),
  ]
)

st.title("Chatbot")
input_text = st.text_input("Enter your question here:")

llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)