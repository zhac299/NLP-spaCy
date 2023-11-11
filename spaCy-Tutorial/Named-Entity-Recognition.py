import spacy 
nlp = spacy.load('en_core_web_sm')

# Create an nlp object
doc = nlp("Indians spent over $71 billion on clothes in 2018")
 
for ent in doc.ents:
    print(ent.text, ent.label_)

print(spacy.explain("NORP"))