import spacy

nlp = spacy.load('en_core_web_sm')

# Create an nlp object
doc = nlp("He went to play basketball")

# Returns active pipeline componenets
print(nlp.pipe_names)

# Disables selected pipeline componenets
# nlp.disable_pipes('tagger', 'parser')