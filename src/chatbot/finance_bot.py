from src.nlp.intent_classifier import IntentClassifier
from src.nlp.entity_extractor import EntityExtractor

class FinanceBot:
    def __init__(self):
        self.intent_classifier = IntentClassifier()
        self.entity_extractor = EntityExtractor()
        self.account_balance = 5000 

    def process_message(self, message):
        intent = self.intent_classifier.predict(message)
        entities = self.entity_extractor.extract_entities(message)
        
        if intent == "check_balance":
            return self.check_balance(entities)
        elif intent == "analyze_spending":
            return self.analyze_spending(entities)
        elif intent == "save_money":
            return self.save_money(entities)
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"

    def check_balance(self, entities):
        return f"Your current account balance is ${self.account_balance:.2f}"

    def analyze_spending(self, entities):
        spending_data = {
            'Food': 300,
            'Rent': 1000,
            'Utilities': 200,
            'Entertainment': 150,
            'Transport': 250
        }
        
        total_spending = sum(spending_data.values())
        top_category = max(spending_data, key=spending_data.get)
        
        analysis = f"Your total spending this month is ${total_spending:.2f}. "
        analysis += f"Your highest spending category is {top_category} at ${spending_data[top_category]:.2f}. "
        
        if 'category' in entities:
            category = entities['category']
            if category in spending_data:
                analysis += f"You've spent ${spending_data[category]:.2f} on {category} this month."
            else:
                analysis += f"I don't have any data for spending on {category}."
        
        return analysis

    def save_money(self, entities):
        if 'amount' in entities:
            amount = float(entities['amount'])
            self.account_balance += amount
            return f"Great! I've added ${amount:.2f} to your savings. Your new balance is ${self.account_balance:.2f}"
        else:
            return "To save money, please specify an amount. For example, 'Sav
