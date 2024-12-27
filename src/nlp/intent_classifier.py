import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

class IntentClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.classifier = MultinomialNB()

    def train(self, X, y):
        X_vec = self.vectorizer.fit_transform(X)
        self.classifier.fit(X_vec, y)

    def predict(self, text):
        X_vec = self.vectorizer.transform([text])
        return self.classifier.predict(X_vec)[0]
