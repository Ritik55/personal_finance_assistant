# main.py
import yaml
from src.chatbot.finance_bot import FinanceBot

def load_config():
    with open('config/config.yaml', 'r') as file:
        return yaml.safe_load(file)

def main():
    config = load_config()
    bot = FinanceBot(config)
    bot.run()

if __name__ == "__main__":
    main()
