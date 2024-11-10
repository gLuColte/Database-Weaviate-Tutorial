import requests
import json
import pandas as pd

# Weaviate server URL
WEAVIATE_URL = "http://localhost:8080/v1/graphql"

def load_vector_from_json(file_path):
    """Load the vector from a JSON file."""
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        # Extract the vector from the JSON data
        return data['properties']['category_similarity']

def get_similar_entries(search_vector, limit=10):
    """Retrieve entries similar to the given vector from Weaviate."""
    query = {
        "query": f"""
        {{
            Get {{
                ImageObject(nearVector: {{vector: {json.dumps(search_vector)}}}, limit: {limit}) {{
                    image_url
                    _additional {{
                        id
                        score
                    }}
                }}
            }}
        }}
        """
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    print("Sending query to Weaviate:")
    
    response = requests.post(WEAVIATE_URL, headers=headers, data=json.dumps(query))
    
    print("Response status code:", response.status_code)  # Debugging line
    print("Response content:", response.content)  # Debugging line
    
    if response.status_code == 200:
        data = response.json()
        entries = data.get('data', {}).get('Get', {}).get('ImageObject', [])
        if entries:
            # Create a DataFrame to display the results
            df = pd.DataFrame(entries)
            print("\nMain entry and similar entries:")
            print(df)
        else:
            print("No similar entries found.")
    else:
        print(f"Failed to retrieve similar entries. Status code: {response.status_code}")
        print("Response:", response.text)

if __name__ == "__main__":
    # Load the vector from the JSON file
    search_vector = load_vector_from_json('entry.json')
    get_similar_entries(search_vector)
