import streamlit as st
import requests

import os
from dotenv import load_dotenv

load_dotenv()

# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")



st.title('Langchain Demo With LLAMA2 API')

input_text1 = st.text_input("write poem")



def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/peom/invoke",
                             json={'input':{'topic':input_text}})
    return response.json()['output']
    

if input_text1:
    st.write(get_ollama_response(input_text1))