from src.pipeline.load import load
from src.pipeline.transform import transform
from src.pipeline.retriever import load_qa_chain
from src.pipeline.prompts import PROMPT_TEMPLATE
from langchain.prompts import PromptTemplate


def load_transform(docs_path: str):
    doc_chunks = load(docs_path)
    vector_store = transform(doc_chunks)
    retriever = vector_store.as_retriever()
    return retriever


def setup(docs_path: str, llm=None):
    prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)
    retriever = load_transform(docs_path)
    chain = load_qa_chain(retriever, llm, prompt)
    return chain
