import spacy

model_test = "would you be pleased if i asked you to open the google chrome"

# load the trained model
nlp_output = spacy.load("nlu/entity_extraction/output/model-best")

# pass our test instance into the trained pipeline
doc = nlp_output(model_test)


# print out the identified entities
for ent in doc.ents:
    if ent.label_ == "APPLICATION":
        print(ent.text, ent.label_)
