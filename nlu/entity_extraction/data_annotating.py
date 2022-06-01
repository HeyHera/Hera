from traceback import print_tb
from tqdm import tqdm
import regex as re
import json

# this dictionary will contain all annotated examples
with open(file='nlu/entity_extraction/nlu_ee_training_data.json', mode='r') as fp:
    collective_dict = json.load(fp)
collective_dict = {'TRAINING_DATA': []}


def structure_training_data(text, kw_list, entity_label):
    results = []
    entities = []

    # search for instances of keywords within the text (ignoring letter case)
    for kw in tqdm(kw_list):
        search = re.finditer(kw, text, flags=re.IGNORECASE)

        # store the start/end character positions
        all_instances = [[m.start(), m.end()] for m in search]

        # if the callable_iterator found matches, create an 'entities' list
        if len(all_instances) > 0:
            for i in all_instances:
                start = i[0]
                end = i[1]
                entities.append((start, end, entity_label))

        # alert when no matches are found given the user inputs
        else:
            print("No pattern matches found. Keyword:", kw)

    # add any found entities into a JSON format within collective_dict
    if len(entities) > 0:
        results = [text, {"entities": entities}]
        collective_dict['TRAINING_DATA'].append(results)
        return


if __name__ == '__main__':
    with open(file="nlu/entity_extraction/spacy_train_text.txt", mode='r', encoding='utf-8') as spacy_train_text:
        text = spacy_train_text.read()
    kw_list = ['from downloads to documents', 'from music to downloads', 'from documents to pictures', 'from documents to music', 'from music to downloads', 'from pictures to downloads', 'from home to pictures', 'from documents to documents', 'from documents to config', \
                'from config to home', 'in downloads', 'in documents', 'in pictures', 'from new folder to documents', 'from music to videos', 'from documents to new folder', 'from new folder to music', 'from videos to downloads', 'from pictures to videos', 'from config to pictures', 'from documents to local', \
                    'from local to documents', 'from videos to downloads', 'from videos to music', 'from new folder to downloads', 'from pictures to new folder', 'from videos to new folder', 'in new folder', 'in videos', 'in new folder', 'in local']
    kw_list = set(kw_list)
    entity_label = "FILE_MANIPULATION"
    structure_training_data(text=text, kw_list=kw_list,
                            entity_label=entity_label)
    print("\n{} Result {}".format("="*80, "="*80))
    print(collective_dict)
    try:
        with open("nlu/entity_extraction/nlu_ee_training_data.json", "w") as training_data:
            json.dump(collective_dict, training_data, indent=4)
        print("\nTraining data annotation finished. Saved to nlu/entity_extraction/nlu_ee_training_data.json")
    except Exception as e:
        print("Exception: ", e)
