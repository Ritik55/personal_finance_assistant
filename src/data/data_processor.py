import pandas as pd

class DataProcessor:
    def process_transactions(self, transactions):
        df = pd.DataFrame(transactions)
        df['date'] = pd.to_datetime(df['date'])
        df['amount'] = df['amount'].astype(float)
        return df

    def categorize_expenses(self, df):
        # Implement expense categorization logic here
        pass
