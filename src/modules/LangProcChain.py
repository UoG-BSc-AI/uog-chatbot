import nltk
import spacy
from transformers import BertTokenizer
# import torch
from textblob import TextBlob
from langchain_community.document_loaders import TextLoader
from modules.data_scrape import Scrape_Data, load_docs_from_jsonl

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
docs_scraped_directly = Scrape_Data("././data/discovered_urls.txt")

def lang_processing(text):

    nlp = spacy.load('en_core_web_trf')

    text = str(TextBlob(text).correct())

    doc = nlp(text)

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    tokens = tokenizer.tokenize(text)

    nltk.download('averaged_perceptron_tagger')
    pos_tags = nltk.pos_tag(tokens)

    return pos_tags, doc

import spacy
from textblob import TextBlob

#------------------------------------------------------


text = 'To start cleaning the data, I first imported it into a pandas dataframe and began to look at the data using the head() function. From looking at the data, I could see that the index column needed to be renamed and adjusted to start from 0, and the net_type column had a spelling mistake in the word mobile. Next, I look at the number of null values in the dataset and find that they are only present in the avg_lat_up_ms and avg_lat_down_ms columns. This is explained at the source of the dataset as not all versions of the speed test measure this value. In an attempt to fill these null values, I considered using the interpolate() function in pandas but as the data on each row is separate reading from different devices making them statistically independent from adjacent rows, although the distribution would look correct the correlation between attributes would be damaged, effecting the usefulness of the data for further analysis.'

nlp = spacy.load('en_core_web_trf')

text = str(TextBlob(text).correct())

doc = nlp(text)
pos_tags = [(token.text, token.pos_) for token in doc]

print("POS Tags:", pos_tags)

for ent in doc.ents:
    print(ent.text, ':', ent.label_)