import streamlit as st
from langchain_community.llms import OpenAI
from langchain_community.llms import Ollama
from src.pipeline.inference import setup

st.set_page_config(
    page_title="University of Gloucestershire Chatbot",
    page_icon="🎓",
    layout="wide"
)

apiKey = st.sidebar.text_input('OpenAI API Key')
if not apiKey.startswith('sk-'):
    st.sidebar.warning('Please enter your OpenAI API key!')


def generate_response(prompt):
    llm = OpenAI(temperature=0.5, openai_api_key=apiKey)
    st.info(llm(prompt))


def main():
    llm = Ollama(model="stable-beluga", temperature=0)
    chain = setup(docs_path="data/training/input.json", llm=llm)
    # q = "Describe your purpose and background knowledge"

    st.title('University of Gloucestershire Playground')

    with st.form('my_form'):

        text = st.text_area('Enter text:', '')
        submitted = st.form_submit_button('Submit')

        if submitted and apiKey.startswith('sk-'):
            response = chain({"query": text})
            st.info(response['result'])

        elif submitted:
            response = chain({"query": text})
            st.info(response['result'])


if __name__ == "__main__":
    main()
