"""
Ollama is used to download and run the model.
1. Download Ollama: https://ollama.com/download
2. Download and run the model: https://ollama.com/library

Streamlit is user for the User Interface.
Streamlit Generative AI: https://streamlit.io/generative-ai
Streamlit API Reference: https://docs.streamlit.io/library/api-reference

1. pip install streamlit
2. streamlit run main.py

LangChain is used to communicate with the model.
LangChain: https://python.langchain.com/docs/integrations/toolkits/python
1. pip install langchain

DISCLAIMER: DO NOT FULLY RELY ON THE MODEL OUTPUT.
"""
import streamlit as st
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import PromptTemplate

# Instructions template, where {} will contain the variable of input.
prompt_template = """You are an expert in Ethical Data Science. 
    
Based on the provided user scenario for a project, \
determine whether it requires ethical approval using\
the provided Criteria.

Criteria:
- research which involves biomedical or clinical intervention;
- deceptive research where the investigator actively sets out to misrepresent themselves;
- certain classes of covert research;
- all research where participants are under 18;
- research into sensitive topics;
- research involving vulnerable groups.

You answer should be 'Yes' or 'No', with a full reason for either case.

User scenario: {input}
"""

prompt = PromptTemplate(input_variables=["input"], template=prompt_template)

# Choose the LLM you want to run, change the model to your model version, i,e: gemma:7b
llm = LLMChain(
    llm=Ollama(
        model="gemma:7b",
        base_url="http://localhost:11434",
        callback_manager=CallbackManager(
            [StreamingStdOutCallbackHandler()],
        ),
    ),
    prompt=prompt,
)

st.write("# Ethical Consultant !")

# Take input from the user
query = st.text_input("Enter a query: ")

# Create a button named Enter.
# The code within this If statement is executed if the button is pressed
if st.button("Enter"):
    # The spinner will run until we receive a response from the LLM
    with st.spinner("Thinking..."):
        res = llm.invoke({"input": query})

        # Write the response on to our web page
        st.write(res["text"])