import pandas as pd
from sklearn.cluster import KMeans

class SpendingAnalyzer:
    def __init__(self):
        self.model = KMeans(n_clusters=3)

    def analyze_spending(self, transactions):
        df = pd.DataFrame(transactions)
        features = df[['amount', 'category']]
        self.model.fit(features)
        df['cluster'] = self.model.predict(features)
        return df
