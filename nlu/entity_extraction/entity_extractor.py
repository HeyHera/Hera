import spacy
nlp_output = spacy.load("nlu/entity_extraction/output/model-best")

def extract(model_test_sentence, entity_label):
    doc = nlp_output(model_test_sentence)
    # print out the identified entities
    for ent in doc.ents:
        if ent.label_ == entity_label:
            return(ent.text)

if __name__ == '__main__':
    model_test_sentence = "would you be pleased if i asked you to open the application google chrome"
    entity_label = "APPLICATION"
    pt = extract(model_test_sentence, entity_label)
    print(pt)