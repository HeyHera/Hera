from joblib import load


clf = load('nlu/intent_classification/models/sklearn_intent_classifier.joblib')


def classify(str):
    input_list = []*1
    # type(str) >> string
    input_list.insert(0, str)
    predicted_intents = clf.predict(input_list)
    return(predicted_intents)


if __name__ == '__main__':
    pt = classify('play strong')
    print(pt)
