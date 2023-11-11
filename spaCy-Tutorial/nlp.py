import spacy
nlp = spacy.load('en_core_web_sm')

# Create an nlp object
doc = nlp("He went to play basketball")