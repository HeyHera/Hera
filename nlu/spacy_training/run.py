import spacy

model_test = "At Perfection Landscapes LLC, we are committed to protecting the health of trees \
and shrubs in urban and suburban areas. We work with clients to provide expertise in all areas \
of tree care, stump removal, and construction-related tree preservation. Our trained experts \
also have years of experience with insect control. Call us today for a consultation!"

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
    if ent.label_ == "SERVICE":
        print(ent.text, ent.label_)