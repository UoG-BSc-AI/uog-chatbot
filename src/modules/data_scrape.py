from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer

urls = ['https://www.glos.ac.uk/information/knowledge-base/business-school/']

# Load HTML
loader = AsyncChromiumLoader(urls)
html = loader.load()

# Transform
bs_transformer = BeautifulSoupTransformer()
docs_transformed = bs_transformer.transform_documents(html, tags_to_extract=["p"])

# Result
docs_transformed[0].page_content[0:500]

print(docs_transformed[0])