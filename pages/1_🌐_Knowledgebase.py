import streamlit as st
import pandas as pd

st.set_page_config(page_title="Knowledgebase", page_icon="📈", layout="wide")

st.markdown("# Knowledgebase")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)


df = pd.read_json("data/training/input.json")
df['metadata'] = df['metadata'].apply(lambda x: x['source'])
df['page_content'] = df['page_content'].apply(lambda x: x.split("»")[-1])

st.dataframe(df, use_container_width=True, hide_index=True, height=500)
