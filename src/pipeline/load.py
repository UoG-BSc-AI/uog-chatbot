from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from typing import List, Iterable
import json


def load_documents_from_json(path: str) -> List[Document]:
    documents = []

    # Load JSON file
    with open(path, "r") as file:
        data = json.load(file)

    # Iterate through each item in the JSON array
    for item in data:
        page_content = item["page_content"]
        metadata = item["metadata"]
        documents.append(Document(page_content=page_content, metadata=metadata))

    return documents


def split_documents(
    documents: Iterable[Document], chunk_size: int = 1000, chunk_overlap: int = 20
) -> List[Document]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )

    chunks = text_splitter.split_documents(documents=documents)
    return chunks


def load(path: str) -> List[Document]:
    docs = load_documents_from_json(path)
    split_docs = split_documents(docs)

    return split_docs


if __name__ == "__main__":
    document_chunks = load("../../data/training/input.json")
    print(document_chunks[:2])
