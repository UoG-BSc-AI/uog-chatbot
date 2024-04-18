import streamlit as st
from langchain.llms import OpenAI

apiKey = st.sidebar.text_input('OpenAI API Key')

def generate_response(prompt):
  llm = OpenAI(temperature=0.5, openai_api_key=apiKey)
  st.info(llm(prompt))

def main():
  st.title('OpenAI Playground')
  with st.form('my_form'):
    text = st.text_area('Enter text:', '')
    submitted = st.form_submit_button('Submit')
    if not apiKey.startswith('sk-'):
      st.warning('Please enter your OpenAI API key!')
    if submitted and apiKey.startswith('sk-'):
      generate_response(text)

if __name__ == "__main__":
    main()