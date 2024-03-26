from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
from langchain.schema import Document
import json
from typing import Iterable


"""Pass a txt of urls into method to scrape data from"""
def Scrape_Data(file_path):

    # Open the file in read mode
    with open(file_path, "r", encoding="utf-8") as file:
        # Read all lines from the file into an array, removing newline characters
        urls = [line.strip() for line in file]

    print(urls)

    # Load HTML
    loader = AsyncChromiumLoader(urls)
    html = loader.load()

    # Transform
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(html, tags_to_extract=["p"])

    # print(docs_transformed)
    
    # Example usage:
    output_file = "././data/training/input.json"
     #save_transformed_docs(docs_transformed, output_file)
    save_docs_to_json(docs_transformed, output_file)

    return docs_transformed

def save_transformed_docs(transformed_docs, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        for doc in transformed_docs:
            file.write(doc.page_content + "\n\n")



def save_docs_to_json(array:Iterable[Document], output_file):
    with open(output_file, 'w') as jsonl_file:
        for doc in array:
            jsonl_file.write(doc.json() + '\n')

def load_docs_from_jsonl(file_path)->Iterable[Document]:
    array = []
    with open(file_path, 'r') as jsonl_file:
        for line in jsonl_file:
            data = json.loads(line)
            obj = Document(**data)
            array.append(obj)
    return array


    # Result
    # docs_transformed[0].page_content[0:500]

#print(docs_transformed[0])