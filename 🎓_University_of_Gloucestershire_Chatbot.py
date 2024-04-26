import streamlit as st
from langchain_community.llms import OpenAI
from langchain_community.llms import Ollama
from src.pipeline.inference import setup


#Implemented choice between Ollama and OpenAI models. (uses ollama if no key is entered)
#Im not sure why but my openAI keys dont seem to be working, this may because of my account setup
#If someone could test this it would be great. - Robbie

st.set_page_config(
    page_title="University of Gloucestershire Chatbot",
    page_icon="🎓",
    layout="wide"
)

apiKey = st.sidebar.text_input('OpenAI API Key')
if not apiKey.startswith('sk-'):
    st.sidebar.warning('Please enter your OpenAI API key!')

def generate_response_openai(prompt):

    if not apiKey.startswith('sk-'):
        return "Please enter your OpenAI API key!"
    try:
        llm = OpenAI(temperature=0.5, openai_api_key=apiKey)
        response = llm(prompt)
        return response 
    except Exception as e:
        return f"Invalid Key"

def generate_response_ollama(prompt):
    llm = Ollama(model="stable-beluga", temperature=0)
    chain = setup(docs_path="data/training/input.json", llm=llm)
    response = chain({"query": prompt})
    return response["result"]


def main():
    st.title('University of Gloucestershire Playground')

    response = "Enter Your query here"

    with st.form('my_form'):

        text = st.text_area('Enter text:', '')
        submitted = st.form_submit_button('Submit')

        if submitted:
            if apiKey.startswith('sk-'):
                response = generate_response_openai(text)

            else:
                response = generate_response_ollama(text)
            
        st.info(response)


if __name__ == "__main__":
    main()
