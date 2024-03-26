import nltk
import spacy
from transformers import BertTokenizer
# import torch
from textblob import TextBlob
from langchain_community.document_loaders import TextLoader
from modules.data_scrape import Scrape_Data , load_docs_from_jsonl

# Load dataset that was scraped from UoG Website
#loader = TextLoader("././data/training/input.txt")
docs = load_docs_from_jsonl("././data/training/input.json")
#test :
#print(docs[0].page_content)

# Option 1 - Load data from pre-saved txt
# Save data into document data type variable
#docs = loader.load()

# Option 2 - Scrape data directly using custom scrape function
# Save data into document data type variable

#to run all URLs use discovered_urls.txt
#docs_scraped_directly = Scrape_Data("././data/urls.txt")

def lang_processing(text):

    nlp = spacy.load('en_core_web_trf')

    text = str(TextBlob(text).correct())

    doc = nlp(text)

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    tokens = tokenizer.tokenize(text)

    nltk.download('averaged_perceptron_tagger')
    pos_tags = nltk.pos_tag(tokens)

    return pos_tags, doc

# tokens = ['[CLS]'] + tokens + ['[SEP]']
# input_ids = tokenizer.convert_tokens_to_ids(tokens)
# max_length = 512
# padded_input_ids = input_ids + [tokenizer.pad_token_id] * (max_length - len(input_ids))
# input_tensor = torch.tensor(padded_input_ids).unsqueeze(0)
# model = BertForSequenceClassification.from_pretrained('bert-base-uncased')
# model.config.pad_token_id
# outputs = model(input_tensor)
# logits = outputs[0]
# predictions = torch.argmax(logits, dim=1)

# print(pos_tags)

# for ent in doc.ents:
#     print(ent.text, ':', ent.label_)

# print("Predicted class:", predictions.item())
text = 'The quick brown fox jumped over the lazy dog.'

nlp = spacy.load('en_core_web_trf')

text = str(TextBlob(text).correct())

doc = nlp(text)

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize(text)

nltk.download('averaged_perceptron_tagger')
pos_tags = nltk.pos_tag(tokens)

print(pos_tags)

#Named entity recognition (Work in progress)
for ent in doc.ents:
    print(ent.text, ':', ent.label_)