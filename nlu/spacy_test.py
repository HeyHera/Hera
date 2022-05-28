# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
# text = ("Play the song magic")
text = ("play in the end")
# text = ("open firefox")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
# for entity in doc.ents:
#     print(entity.text, entity.label_)

print("-"*80)
for x in doc :
    if x.pos_ == "NOUN":
        print("Noun", x)
    if x.pos_ == "PROPN":
        print("Proper Noun", x)
    if x.pos_=="PRON":
        print("Pronoun", x)