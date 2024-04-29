import streamlit as st
import pandas as pd

st.set_page_config(page_title="Experiments", page_icon="🧪", layout="wide")

st.markdown("# Experiments")

df = pd.read_csv("data/experiments/experiments_queries.csv")
st.dataframe(df[["Category", "Query"]], hide_index=True)

st.write("""## Ollama - Stable-beluga""")
st.write("""Input, Output""")

st.write("""## OpenAI""")
st.write("""Input, Output""")
