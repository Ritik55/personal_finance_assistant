from src.nlp.intent_classifier import IntentClassifier
from src.nlp.entity_extractor import EntityExtractor

class FinanceBot:
    def __init__(self):
        self.intent_classifier = IntentClassifier()
        self.entity_extractor = EntityExtractor()

    def process_message(self, message):
        intent = self.intent_classifier.predict(message)
        entities = self.entity_extractor.extract_entities(message)
        
        if intent == "check_balance":
            return self.check_balance(entities)
        elif intent == "analyze_spending":
            return self.analyze_spending(entities)
        # Add more intents and corresponding methods

    def check_balance(self, entities):
        # Implement balance checking logic
        pass

    def analyze_spending(self, entities):
        # Implement spending analysis logic
        pass
