import spacy
from tqdm import tqdm
import json
from spacy.tokens import DocBin

# define our training data to TRAIN_DATA
with open(file='nlu/spacy_training/training_data.json', mode='r') as fp:
    collective_dict = json.load(fp)
TRAIN_DATA = collective_dict['TRAINING_DATA']

# create a blank model
nlp = spacy.blank('en')


def create_training_set(TRAIN_DATA):
    db = DocBin()
    for text, annot in tqdm(TRAIN_DATA):
        doc = nlp.make_doc(text)
        ents = []

        # create span objects
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label,
                                 alignment_mode="contract")

            # skip if the character indices do not map to a valid span
            if span is None:
                print("Skipping entity.")
            else:
                ents.append(span)
                # handle erroneous entity annotations by removing them
                try:
                    doc.ents = ents
                except:
                    # print("BAD SPAN:", span, "\n")
                    ents.pop()
        doc.ents = ents

        # pack Doc objects into DocBin
        db.add(doc)
    return db


TRAIN_DATA_DOC = create_training_set(TRAIN_DATA)

# Export results (here I add it to a TRAIN_DATA folder within the directory)
TRAIN_DATA_DOC.to_disk("nlu/spacy_training/TRAIN_DATA_train.spacy")
