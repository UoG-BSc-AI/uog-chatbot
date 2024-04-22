import textwrap

from langchain_community.llms import Ollama

from src.pipeline.inference import setup


def main():
    llm = Ollama(model="stable-beluga", temperature=0)
    chain = setup(docs_path="../../data/training/input.json", llm=llm)
    q = "Describe your purpose and background knowledge"

    while not q.lower() == "quit":
        response = chain({"query": q})
        print(textwrap.fill(response["result"], width=100))
        q = input("What is your query? >> ")


if __name__ == "__main__":
    main()
