# [spaCy](https://spacy.io/)
### Reference
[Auto-Detect Anything With Custom Named Entity Recognition (NER)](https://levelup.gitconnected.com/auto-detect-anything-with-custom-named-entity-recognition-ner-c89d6562e8e9)  

## WHAT is NER?

NER is a growing area of Natural Language Processing that aims to accurately locate and classify key information within text.

## spaCy
spaCy is an industrial-strength Natural Language Processing package in Python.

## Installing
```
pip install spacy
```
```
python -m spacy download en_core_web_sm
```
## Steps
### Step #1: Data Annotation
1. Add text to `spacy_train_text.txt`.
2. Modify the keywords in `data_annotating.py`.

### Step #2: Converting JSON format to spaCy Doc objects
1. Run `json_to_doc_object.py`

### Step #3: Training
1. Add a `base_config.cfg` file with ner selected from [here](https://spacy.io/usage/training).
2. If already the file is present, go to next step.
3. Open `base_config.cfg` and modify the train and dev parameters as
```
train = "./TRAIN_DATA.spacy"
dev = "./TRAIN_DATA.spacy"
```
### Step #4 
Run 
```
python -m spacy init fill-config ./base_config.cfg ./config.cfg
```
### Step #5 
Next, run the following to begin training
```
python -m spacy train config.cfg --output ./output
```
After training is complete, the resulting model will appear in a new folder called output.