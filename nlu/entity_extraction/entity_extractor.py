import spacy

def extract(model_test_sentence, entity_label, model_path):
    nlp_output = spacy.load(model_path)
    doc = nlp_output(model_test_sentence)
    # print out the identified entities
    for ent in doc.ents:
        if ent.label_ == entity_label:
            return(ent.text)

if __name__ == '__main__':
    model_test_sentence = "play the song from grandmaster"
    entity_label = "MUSIC"
    model_path = "nlu/entity_extraction/output/music_playback/model-best"
    pt = extract(model_test_sentence, entity_label, model_path)
    print(pt)