import requests
import csv

class PublicAPIClient:
    def __init__(self, base_url: str, client_id: str, client_secret: str):
        self.base_url = base_url
        self.token = self.get_bearer_token(client_id, client_secret)

    def get_bearer_token(self, client_id: str, client_secret: str) -> str:
        # URL to request the access token from
       auth_url = "https://api.salesforce.com/oauth/token"

        #  Data we send in the POST request to get the token
        payload = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret
        }

        response = requests.post(auth_url, data=payload) # Send a POST request to get the token
        response.raise_for_status()

        # Extract the access token from the JSON response
        access_token = response.json()["access_token"]

    def pull_all_contacts(self) -> list:
        page_number = 1 # Start from page 1
        all_contacts = [] # List to store all contact records

        while True:
            url = f"{self.base_url}?page={page_number}"
            # Add the Bearer token in the headers to authorize the request
            headers = {"Authorization": f"Bearer {self.token}"}

            try:
                response = requests.get(url, headers=headers) # Send the GET request to the current page
                response.raise_for_status() # Stop if status code is error (e.g., 404, 500)
                page_data = response.json().get("data", [])

                if not page_data:
                    break
                # Add all contacts from this page to the main list then move to next page
                all_contacts.extend(page_data)
                page_number += 1

            except requests.exceptions.RequestException as error:
                print(f"Failed to fetch page {page_number}: {error}")
                break

        return all_contacts

    def save_contacts_to_csv(self, contacts: list, filename: str):
        if not contacts:
            print("No contacts to save.")
            return

        with open('contacs.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=contacts[0].keys())
            writer.writeheader()
            writer.writerows(contacts)

def main():
    # This is fake data just for demo. Replace with real Salesforce details later.
    client_id = "FAKE_ID"
    client_secret = "FAKE_SECRET"
    base_url = "https://reqres.in/api/users"

    client = PublicAPIClient(base_url, client_id, client_secret)
    contacts = client.pull_all_contacts()
    client.save_contacts_to_csv(contacts, "contacts.csv")

if __name__ == "__main__":
    main()

