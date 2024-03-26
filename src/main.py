import streamlit as st
from langchain.llms import OpenAI
#import modules.LangProcChain as bot

"""

Changes:
        -generate response done by sams model (lang_processing)
        -api removed (wasnt sure why we needed it)
"""

#https://docs.streamlit.io/knowledge-base/tutorials/llm-quickstart

#webpage title
st.title("UoG Chatbot")

with st.form('form_1'):
    text = st.text_area('Enter text:', 'How do i get an assignment reassessed?')
    #submitted = boolean if button is clicked
    submitted = st.form_submit_button('Enter')
    #if submitted:
        #run sams model and write the response
        #response = bot.lang_processing(text)
        #st.write(response)
   