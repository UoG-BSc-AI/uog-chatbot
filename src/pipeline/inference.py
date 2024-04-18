from src.load import load
from src.transform import transform
from src.retriever import load_qa_chain
from src.prompts import PROMPT_TEMPLATE
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate


def load_transform(docs_path: str):
    doc_chunks = load(docs_path)
    vector_store = transform(doc_chunks)
    retriever = vector_store.as_retriever()
    return retriever


def setup(docs_path: str):
    llm = Ollama(model="stable-beluga", temperature=0)
    prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)
    retriever = load_transform(docs_path)
    chain = load_qa_chain(retriever, llm, prompt)
    return chain
