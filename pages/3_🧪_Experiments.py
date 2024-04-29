import streamlit as st
import pandas as pd

st.set_page_config(page_title="Experiments", page_icon="🧪", layout="wide")

st.markdown("# Experiments")

df = pd.read_csv("data/experiments/experiments_queries.csv")
st.dataframe(df[["Category", "Query"]], hide_index=True)

st.write("""## [Llama3](https://ollama.com/library/llama3)""")
st.dataframe(df[["Category", "Query"]], hide_index=True)

st.write("""## [Stable-beluga](https://ollama.com/library/stable-beluga)""")
st.dataframe(df[["Category", "Query"]], hide_index=True)
