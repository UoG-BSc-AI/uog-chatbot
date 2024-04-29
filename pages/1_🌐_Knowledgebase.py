import pandas as pd
import streamlit as st

st.set_page_config(page_title="Knowledgebase", page_icon="📈", layout="wide")

st.markdown("# Knowledgebase")
st.write(
    """The dataset scraped from the University Knowledge base."""
)


df = pd.read_json("data/training/input.json")
df["metadata"] = df["metadata"].apply(lambda x: x["source"])
df["page_content"] = df["page_content"].apply(lambda x: x.split("»")[-1])

st.dataframe(df, use_container_width=True, hide_index=True, height=500)
