from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from modules.data_scrape import load_docs_from_jsonl


class Document:
    def __init__(self, text):
        self.text = text

def retrieve_documents(query, documents, vectorizer):
    query_vector = vectorizer.transform([query])
    document_vectors = vectorizer.transform([doc.text for doc in documents])
    similarities = (query_vector * document_vectors.T).A[0]
    sorted_indices = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)
    return [documents[i] for i in sorted_indices[:3]]  # Return top 3 most relevant documents

def generate_response(query, retrieved_documents):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    input_ids = tokenizer.encode(query + " " + retrieved_documents[0].text, return_tensors="pt", max_length=1024)
    output = model.generate(input_ids, max_length=50, num_return_sequences=1, early_stopping=True)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

def main():
    # Load documents from JSON Lines file
    global documents
    documents = load_docs_from_jsonl("././data/training/input.json")



def gen_response(query):

    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit vectorizer on document texts
    vectorizer.fit([doc.text for doc in documents])

    # Retrieve relevant documents
    retrieved_documents = retrieve_documents(query, documents, vectorizer)

    # Generate response based on retrieved documents and user query
    response = generate_response(query, retrieved_documents)

    print("Response:", response)


if __name__ == "__main__":
    main()
