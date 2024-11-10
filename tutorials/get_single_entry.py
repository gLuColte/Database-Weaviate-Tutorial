import requests
import json

# Weaviate server URL
WEAVIATE_URL = "http://localhost:8080/v1/objects"

def get_entry_by_uuid(entry_uuid):
    """Retrieve an entry from Weaviate by its UUID and save the details to a JSON file."""
    url = f"{WEAVIATE_URL}/ImageObject/{entry_uuid}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Save the entry to a JSON file
        with open('entry.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)
        print("Entry saved to entry.json")
    elif response.status_code == 404:
        print(f"Entry with UUID {entry_uuid} not found. Status code: {response.status_code}")
    else:
        print(f"Failed to retrieve entry. Status code: {response.status_code}")
        print("Response:", response.text)

if __name__ == "__main__":
    # Replace 'your_entry_uuid' with the actual UUID you want to retrieve
    # entry_uuid = "01291672-d056-4cf1-bead-ed16a088bd25"
    entry_uuid = "00535cef-d6f8-4c5c-be6f-b31969728667"
    get_entry_by_uuid(entry_uuid)