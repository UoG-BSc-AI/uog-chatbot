import streamlit as st
from langchain_community.llms import OpenAI
from langchain_community.llms import Ollama
from src.pipeline.inference import setup

apiKey = st.sidebar.text_input('OpenAI API Key')


def generate_response(prompt):
    llm = OpenAI(temperature=0.5, openai_api_key=apiKey)
    st.info(llm(prompt))


def main():
    # llm = Ollama(model="stable-beluga", temperature=0)
    # chain = setup(docs_path="data/training/input.json", llm=llm)
    # q = "Describe your purpose and background knowledge"

    st.title('OpenAI Playground')
    # with st.form('my_form'):
    #     text = st.text_area('Enter text:', '')
    #     submitted = st.form_submit_button('Submit')
    #     if not apiKey.startswith('sk-'):
    #         st.warning('Please enter your OpenAI API key!')
    #
    #     if submitted and apiKey.startswith('sk-'):
    #         response = chain({"query": text})
    #         st.info(response)


if __name__ == "__main__":
    main()
