# from sklearn.naive_bayes import MultinomialNB

# X = [
#     'play some music',
#     'play any music',
#     'play a song',
#     'play a random song',
#     'please play a random song',
#     'play a song at random',
#     'play some random music',
#     'play some random song',
#     'play any song',
#     'play some random songs',
#     'play any songs',
#     'would you please play a random music',
#     'would you please play a random song',
#     'play the song',
#     'play the music',
#     'please play the song',
#     'play',
#     'would you please play the song'
# ]

# y = [
#     'rand_song',
#     'rand_song',
#     'rand_song',
#     'rand_song',
#     'rand_song',
#     'rand_song',
#     'rand_song',
#     'rand_song',
#     'rand_song',
#     'rand_song',
#     'rand_song',
#     'rand_song',
#     'rand_song',
#     'spec_song',
#     'spec_song',
#     'spec_song',
#     'spec_song',
#     'spec_song'
# ]

# if len(X) == len(y):
#     print("X, y length matched")

# clf = MultinomialNB()
# clf.fit(X, y)

# print(clf.predict('play in the end'))

import numpy as np
rng = np.random.RandomState(1)
X = rng.randint(5, size=(6, 100))
print(X)
y = np.array([1, 2, 3, 4, 5, 6])
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(X, y)

print(clf.predict(X[2:3]))