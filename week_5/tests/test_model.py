from week_5.model import SpamClassifier
from week_5.config import MODEL_DATA_PATH


def test_model_trains_and_predicts():
    clf = SpamClassifier()
    acc = clf.train(MODEL_DATA_PATH)
    assert acc > 0.8

    spam_label = clf.predict("WINNER! Claim your free prize now")
    ham_label = clf.predict("Hey, are we still on for tomorrow?")

    assert spam_label in (0, 1)
    assert ham_label in (0, 1)
