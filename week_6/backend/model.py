
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


class SpamClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.model = LogisticRegression(max_iter=1000)

    def load_data(self, path: str):
        df = pd.read_csv(
            path,
            sep="\t",
            header=None,
            names=["label", "text"],
            encoding="latin-1",
        )
        df["label"] = df["label"].map({"ham": 0, "spam": 1})
        return df

    def train(self, csv_path: str):
        df = self.load_data(csv_path)
        X = df["text"]
        y = df["label"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        X_train_vec = self.vectorizer.fit_transform(X_train)
        X_test_vec = self.vectorizer.transform(X_test)

        self.model.fit(X_train_vec, y_train)

        y_pred = self.model.predict(X_test_vec)
        acc = accuracy_score(y_test, y_pred)

        print(f"Training done. Accuracy: {acc:.2f}")
        print(classification_report(y_test, y_pred))
        return acc

    def predict(self, message: str) -> int:
        X_vec = self.vectorizer.transform([message])
        return int(self.model.predict(X_vec)[0])
