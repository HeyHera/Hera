from rasa.shared.nlu.training_data.loading import load_data
from rasa.engine.storage.resource import Resource
# from rasa.nlu.model import Trainer
import rasa

from rasa.engine.storage.storage import ModelStorage

# train_data = load_data('natural-language-understanding/datasets/rasa-dataset.json')
# trainer = rTrainer(config.load("config_spacy.yaml"))
# trainer = rasa.nlu.rasa.train(domain='natural-language-understanding/models', config='natural-language-understanding/spacy_backend/config_spacy.yaml', training_files='natural-language-understanding/datasets/rasa-dataset.json')
# interpreter = trainer.train(train_data)
# model_directory = trainer.persist("natural-language-understanding/models", fixed_model_name="current")

trainer = rasa.train(domain='natural-language-understanding/models', config='natural-language-understanding/spacy_backend/config_spacy.yaml', training_files='natural-language-understanding/datasets/rasa-dataset.json')
model_directory = ModelStorage.create("natural-language-understanding/models")
