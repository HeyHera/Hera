import json
from sklearn.pipeline import Pipeline
# Stochastic Gradient Descent (SGD) linear classifier like SVM
from sklearn.linear_model import SGDClassifier
# To convert to Tensorflow matrix model
from sklearn.feature_extraction.text import TfidfVectorizer
from joblib import dump

with open(file="nlu/intent_classification/nlu_ic_training_dataset.json", mode="r", encoding="utf-8") as training_data:
    intent_dict = json.load(training_data)

# X is the sample sentences
X = list(intent_dict.keys())

# y is the intent class corresponding to sentences in X
y = list(intent_dict.values())

# Define the classifier
clf = Pipeline(
    [
        ('tfidf', TfidfVectorizer()),
        ('sgd', SGDClassifier())
    ]
)
# Train the classifier

clf.fit(X, y)
print("Model training complete")
try:
    dump(clf, 'nlu/intent_classification/models/sklearn_intent_classifier.joblib')
    print("Model saved as nlu/intent_classification/models/sklearn_intent_classifier.joblib")
except Exception as e:
    print("Error in saving the model", e)
