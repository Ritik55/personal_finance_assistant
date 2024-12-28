import pandas as pd

class DataProcessor:
    def __init__(self):
        self.category_keywords = {
            'Food': ['restaurant', 'grocery', 'cafe', 'food'],
            'Transport': ['uber', 'lyft', 'taxi', 'bus', 'train', 'gas', 'fuel'],
            'Utilities': ['electricity', 'water', 'gas', 'internet', 'phone'],
            'Entertainment': ['movie', 'theatre', 'concert', 'streaming'],
            'Shopping': ['amazon', 'walmart', 'target', 'clothing', 'electronics']
        }

    def process_transactions(self, transactions):
        df = pd.DataFrame(transactions)
        df['date'] = pd.to_datetime(df['date'])
        df['amount'] = df['amount'].astype(float)
        return df

    def categorize_expenses(self, df):
        def assign_category(description):
            description = description.lower()
            for category, keywords in self.category_keywords.items():
                if any(keyword in description for keyword in keywords):
                    return category
            return 'Other'

        df['category'] = df['description'].apply(assign_category)
        return df

    def analyze_spending(self, df):
        spending_by_category = df.groupby('category')['amount'].sum().sort_values(ascending=False)
        total_spending = spending_by_category.sum()
        spending_percentages = (spending_by_category / total_spending * 100).round(2)

        return {
            'total_spending': total_spending,
            'spending_by_category': spending_by_category.to_dict(),
            'spending_percentages': spending_percentages.to_dict()
        }
