from langchain_community.llms import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

# from langchain.llms import OpenAI
# import model as bot
# https://docs.streamlit.io/knowledge-base/tutorials/llm-quickstart

# load environment variables from .env
load_dotenv()

# get API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# webpage title
st.title("UoG Chatbot")

# sidebar text field for users' OpenAI key
api_key_input = st.sidebar.text_input("OpenAI API Key", value=api_key)


# function connecting to OpenAI model via Langchain
def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=api_key_input)
    st.info(llm(input_text))


with st.form("form_1"):
    text = st.text_area("Enter text:", "How do i get an assignment reassessed?")
    submitted = st.form_submit_button("Enter")

    # API key validation
    if not api_key_input.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")

    # if submit button pressed and API key is valid:
    if submitted and api_key_input.startswith("sk-"):
        generate_response(text)

course_button = st.button("Courses 📔", help="Courses offered at the university.")
student_help_button = st.button("Student Help 🚆", help="Talk to someone.")
