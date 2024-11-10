import weaviate
import json
import pandas as pd
from weaviate.classes.query import MetadataQuery

# Initialize the Weaviate client
client = weaviate.connect_to_local(
    host="localhost",  # Replace with your Weaviate Cloud URL
    port=8080,
    grpc_port=50051
)

imageObject = client.collections.get("ImageObject")

def load_vector_from_json(file_path):
    """Load the vector from a JSON file."""
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        # Extract the vector from the JSON data
        return data['vector']

if __name__ == "__main__":
    response = imageObject.query.near_vector(
        near_vector=load_vector_from_json('entry.json'),
        distance=0.009,
        limit=50,
        return_metadata=MetadataQuery(distance=True)
    )

    # Collect data into a list of dictionaries
    results = []
    for o in response.objects:
        results.append({
            "image_url": o.properties.get("image_url"),
            "distance": o.metadata.distance
        })

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(results)
    print("\nMain entry and similar entries:")
    print(df)

    client.close()