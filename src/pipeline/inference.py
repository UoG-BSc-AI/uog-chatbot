from src.pipeline.load import load
from src.pipeline.transform import transform
from src.pipeline.retriever import load_qa_chain
from src.pipeline.prompts import PROMPT_TEMPLATE
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate


def load_transform(docs_path: str):
    doc_chunks = load(docs_path)
    vector_store = transform(doc_chunks)
    retriever = vector_store.as_retriever()
    return retriever


def setup(docs_path: str):
    # One can specify a different model at this point. For using OpenAI, you might have todo other imports, please refer to langchain docs.
    llm = Ollama(model="stable-beluga", temperature=0)
    prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)
    retriever = load_transform(docs_path)
    chain = load_qa_chain(retriever, llm, prompt)
    return chain
