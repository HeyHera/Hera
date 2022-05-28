from sklearn.pipeline import Pipeline
# Stochastic Gradient Descent (SGD) linear classifier for SVM
from sklearn.linear_model import SGDClassifier
# To convert to Tensorflow matrix model
from sklearn.feature_extraction.text import TfidfVectorizer

# Training data
# X is the sample sentences
X = [
    'play some music',
    'play any music',
    'play a song',
    'play a random song',
    'please play a random song',
    'play a song at random',
    'play some random music',
    'play some random song',
    'play any song',
    'play some random songs',
    'play any songs',
    'would you please play a random music',
    'would you please play a random song',
    'play the song',
    'play the music',
    'please play the song',
    'play',
    'would you please play the song'
]

# y is the intent class corresponding to sentences in X
y = [
    'rand_song',
    'rand_song',
    'rand_song',
    'rand_song',
    'rand_song',
    'rand_song',
    'rand_song',
    'rand_song',
    'rand_song',
    'rand_song',
    'rand_song',
    'rand_song',
    'rand_song',
    'spec_song',
    'spec_song',
    'spec_song',
    'spec_song',
    'spec_song'
]

if len(X) == len(y):
    print("X, y length matched")

# Define the classifier
clf = Pipeline(
    [
        ('tfidf', TfidfVectorizer()),
        ('sgd', SGDClassifier())
    ]
)

# Train the classifier

clf.fit(X, y)

# Test your classifier

# New sentences (that weren't in X and your model never seen before)

new_sentences = [
    'play in the end'
]

predicted_intents = clf.predict(new_sentences)

print(predicted_intents)
