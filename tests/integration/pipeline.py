import pandas as pd
from langchain_community.llms import Ollama, OpenAI

from src.pipeline.inference import setup


def generate_response_ollama(prompt):
    llm = Ollama(model="stable-beluga", temperature=0)
    chain = setup(docs_path="../../data/training/input.json", llm=llm)
    response = chain.invoke({"query": prompt})
    return response["result"]


if __name__ == "__main__":
    df = pd.read_csv("../../data/experiments/experiments_queries.csv")
    df["response"] = df["Query"].apply(lambda x: generate_response_ollama(x))
    df.to_csv("../../data/experiments/experiments_ollama_stable_beluga.csv", index=None)
