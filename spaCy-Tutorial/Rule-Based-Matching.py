import spacy
nlp = spacy.load('en_core_web_sm')

# Import spaCy Matcher
from spacy.matcher import Matcher

# Initialize the matcher with the spaCy vocabulary
matcher = Matcher(nlp.vocab)

doc = nlp("Some people start their day with lemon water")

# Define rule
#Let’s say we want to extract the phrase “lemon water” from the text. 
# So, our objective is that whenever “lemon” is followed by the word 
# “water”, then the matcher should be able to find this pattern in the
# text. That’s exactly what we have done while defining the pattern 
# in the code above. Finally, we add the defined rule to the matcher 
# object.
pattern = [{'TEXT': 'lemon'}, {'TEXT': 'water'}]

# Add rule
matcher.add('rule_1', [pattern])

matches = matcher(doc)
#The output has three elements. 
# The first element, ‘7604275899133490726’, is the match ID. 
# The second and third elements are the positions of the matched tokens.
print(matches)

# Extract matched text
for match_id, start, end in matches:
    # Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)