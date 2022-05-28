import spacy

model_test = "please open the application notepad"

# load the trained model
nlp_output = spacy.load("nlu/spacy_training/output/model-best")

# pass our test instance into the trained pipeline
doc = nlp_output(model_test)

# # customize the label colors
# colors = {"SERVICE": "linear-gradient(90deg, #E1D436, #F59710)"}
# options = {"ents": ["SERVICE"], "colors": colors}

# # visualize the identified entities
# displacy.render(doc, style="ent", options=options)

# print out the identified entities
for ent in doc.ents:
    if ent.label_ == "APPLICATION":
        print(ent.text, ent.label_)