import streamlit as st
import pandas as pd

st.set_page_config(page_title="Experiments", page_icon="🧪", layout="wide")

st.markdown("# Experiments")
st.write("The pipeline was tested with open-source models to evaluate for model response safety and responsibility.")

st.write("""## Dataset""")
st.write("Test dataset credits: ChatGPT")
df = pd.read_csv("data/experiments/experiments_queries.csv")
st.dataframe(df[["Category", "Query"]], hide_index=True)

st.write("""## [Llama3](https://ollama.com/library/llama3)""")
df = pd.read_csv("data/experiments/experiments_ollama_stable_beluga.csv")
df = df.rename(columns={"response": "Model response"})
st.dataframe(df[["Category", "Query", "Model response"]], hide_index=True)

st.write("""## [Stable-beluga](https://ollama.com/library/stable-beluga)""")
df = pd.read_csv("data/experiments/experiments_ollama_stable_beluga.csv")
df = df.rename(columns={"response": "Model response"})
st.dataframe(df[["Category", "Query", "Model response"]], hide_index=True)
