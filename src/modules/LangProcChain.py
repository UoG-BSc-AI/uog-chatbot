import spacy
from textblob import TextBlob


def lang_processing(text):

    nlp = spacy.load('en_core_web_trf')

    text = str(TextBlob(text).correct())

    doc = nlp(text)
    pos_tags = [(token.text, token.pos_) for token in doc]

    return pos_tags, doc
