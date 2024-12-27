import pandas as pd
from sklearn.ensemble import RandomForestRegressor

class SavingsRecommender:
    def __init__(self):
        self.model = RandomForestRegressor()

    def train(self, X, y):
        self.model.fit(X, y)

    def recommend_savings(self, user_data):
        prediction = self.model.predict(user_data)
        return prediction[0]
