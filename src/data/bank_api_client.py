import requests

class BankAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.bank.com/v1"

    def get_transactions(self, account_id):
        endpoint = f"{self.base_url}/accounts/{account_id}/transactions"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(endpoint, headers=headers)
        return response.json()
