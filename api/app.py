from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from langchain_community.llms import Ollama
import uvicorn
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

app=FastAPI(
  title= "Chatbot",
  description= "Chatbot API",
  version= "0.1.0")
llm=Ollama(model="llama3.2")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")

add_routes(
    app,
    prompt1|llm,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
