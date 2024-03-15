import streamlit as st
from langchain.llms import OpenAI

#https://docs.streamlit.io/knowledge-base/tutorials/llm-quickstart

#webpage title
st.title("UoG Chatbot")

#sidebar text field for users' OpenAI key
api_key = st.sidebar.text_input('OpenAI API Key', type='password')

#function connecting to OpenAI model via Langchain
def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key = api_key)
    st.info(llm(input_text))


with st.form('form_1'):
    text = st.text_area('Enter text:', 'How do i get an assignment reassessed?')
    submitted = st.form_submit_button('Enter')

    #API key validation
    if not api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')

    #if submit button pressed and API key is valid:
    if submitted and api_key.startswith('sk-'):
        generate_response(text)