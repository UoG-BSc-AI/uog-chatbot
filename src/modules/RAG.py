from langchain.schema import Document
from langchain.vectorstores import VectorStore
from langchain.embeddings import GPT4AllEmbeddings
from langchain.llms import GPT4All
from modules.data_scrape import load_docs_from_jsonl


# Define a function to retrieve relevant documents based on user query
def retrieve_documents(query, documents, vector_store):
    query_embedding = GPT4AllEmbeddings().embed(query)
    document_embeddings = [GPT4AllEmbeddings().embed(doc.text) for doc in documents]
    similarities = vector_store.compute_similarities(query_embedding, document_embeddings)
    sorted_indices = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)
    return [documents[i] for i in sorted_indices[:3]]  # Return top 3 most relevant documents

# Define a function to generate a response based on retrieved documents and user query
def generate_response(query, retrieved_documents):
    # Combine retrieved documents and user query to generate response
    context = ' '.join([doc.text for doc in retrieved_documents])
    response = GPT4All().generate(prompt=query, context=context, max_tokens=50)
    return response

# Example usage
def main():
    # Load documents from JSON Lines file
    documents = load_docs_from_jsonl("your_dataset.jsonl")

    # Initialize vector store for retrieval
    vector_store = VectorStore(documents)

    # User query
    query = "What is the capital of France?"

    # Retrieve relevant documents
    retrieved_documents = retrieve_documents(query, documents, vector_store)

    # Generate response based on retrieved documents and user query
    response = generate_response(query, retrieved_documents)

    print("Response:", response)

if __name__ == "__main__":
    main()



# "././data/training/input.json"