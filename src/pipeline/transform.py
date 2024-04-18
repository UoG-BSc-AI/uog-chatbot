from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain_core.documents import Document
from typing import (
    List,
)


def load_embedding_model(model_path, normalize_embedding=True):
    return HuggingFaceEmbeddings(
        model_name=model_path,
        model_kwargs={'device': 'cpu'},
        encode_kwargs={
            'normalize_embeddings': normalize_embedding
        }
    )


def create_embeddings(chunks, embedding_model, storing_path='../data/vector_store'):
    vectorstore = FAISS.from_documents(chunks, embedding_model)
    vectorstore.save_local(storing_path)
    return vectorstore


def transform(
        documents: List[Document],
        model_path: str = 'all-MiniLM-L6-v2',
):
    embed = load_embedding_model(model_path=model_path)
    vectorstore = create_embeddings(documents, embed)
    return vectorstore


if __name__ == "__main__":
    from load import load

    doc_chunks = load("../data/training/input.json")
    vector_store = transform(doc_chunks)
    print(type(vector_store))
