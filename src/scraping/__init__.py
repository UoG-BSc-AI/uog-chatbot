from typing import Iterable, List

from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


def load_documents_from_directory(path: str) -> List[Document]:
    loader = PyPDFDirectoryLoader(path)
    docs = loader.load()
    return docs


def split_documents(
    documents: Iterable[Document], chunk_size: int = 1000, chunk_overlap: int = 20
) -> List[Document]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )

    chunks = text_splitter.split_documents(documents=documents)
    return chunks


def load(path: str) -> List[Document]:
    docs = load_documents_from_directory(path)
    split_docs = split_documents(docs)

    return split_docs


if __name__ == "__main__":
    document_chunks = load("../resources/data")
    print(document_chunks[:2])
