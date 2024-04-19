from src.pipeline.inference import setup
import textwrap
import streamlit as st

#Todo:

#if we use openai we need a key which can be created from website 
#allow user to add key to run model
#write text while processing 
#response is created from running main which i assume is the model run script and would return a response if it doesnt work like that then needs changing

def GUI():

    st.title("UOG Chatbot")

    with st.chat_message("user"):
        st.write("What is your query")

    # initialise chat history 
    if "messages" not in st.session_state:
        st.session_state.messsages = []

    #displaying chat messages from on history 
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    #Reacting to user input 
    prompt = st.chat_input("What is your query ")
    if prompt:
        #write the users prompt into the UI
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        #call the model to get a response from prompt
        response = main(prompt)
        
        #display response in chat UI
        with st.chat_message("assistant"):
            st.markdown(response)
        #add the response to chat history 
        st.session_state_messages.append({"role": "assistant", "content": response})


def main(q):
    chain = setup(docs_path="../data/training/input.json")
    q = "Describe your purpose and background knowledge"

    while not q.lower() == "quit":
        response = chain({"query": q})
        print(textwrap.fill(response["result"], width=100))
        q = input("What is your query? >> ")

    return response

if __name__ == "__main__":
    GUI()