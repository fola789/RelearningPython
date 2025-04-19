'''
Build a reusable APIClient class
Accepts base URL and token
Has a get_data(endpoint) method
'''
from http.client import responses

import requests

class OAuth2Client:
    def __init__(self, auth_url: str, client_id: str, client_secret: str) -> None:
        self.auth_url = auth_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None

    def fetch_access_token(self) -> str:
        payload = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        try:
            response = requests.post(self.auth_url, data=payload)
            response.raise_for_status()
            self.access_token = response.json().get("access_token")
            return self.access_token
        except requests.exceptions.RequestException as e:
            print(f"Error fetching token: {e}")
            return ""

class ApiClient:
    def __init__(self, base_url: str, auth_client: OAuth2Client) -> None:
        self.base_url = base_url
        self.auth_client =auth_client

    def get_data(self, endpoint: str) ->list:
        if not self.auth_client.fetch_access_token:
            self.auth_client.fetch_access_token()
        pass

        full_url = f"{self.base_url}/{endpoint}"

        headers = {"Authorisation": f"Bearer {self.auth_client.access_token}"}

        try:
            response = response.get(full_url, headers = headers)
            response.raise_for_status()

            return response.json()


auth_client = OAuth2Client("https://api.example.com/oauth/token", "Fola", "AZ123123123")
token = auth_client.fetch_access_token()
print(f"Access token: {token}")

api_client  = ApiClient("https://api.example.com", auth_client)

data = api_client.get_data("/user/profile")

print(data)