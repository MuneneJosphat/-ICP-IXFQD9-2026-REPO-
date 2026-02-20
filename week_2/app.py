from model import SpamClassifier

DATA_PATH = "week_2/data/SMSSpamCollection"


def main():
    clf = SpamClassifier()
    clf.train(DATA_PATH)

    print(" Spam CLI ")
    print("Type a message to classify, or 'q' to quit.\n")

    while True:
        text = input("Message: ").strip()
        if text.lower() in {"q", "quit", "exit"}:
            break

        label = clf.predict(text)
        if label == 1:
            print("=> Prediction: SPAM\n")
        else:
            print("=> Prediction: NOT SPAM\n")


if __name__ == "__main__":
    main()
