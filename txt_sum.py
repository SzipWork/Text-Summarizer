from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()
llm = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

st.header('Text Summarizer')

user_input = st.text_input("Write your prompt")

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


template = load_prompt('template.json')




if st.button('Summarize'):
    chain = template | llm
    result = chain.invoke({
    "paper_input": user_input,
    "style_input": style_input,
    'length_input': length_input
})
    st.write(result.content)