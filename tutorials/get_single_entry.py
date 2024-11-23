import weaviate
import json
import argparse

client = weaviate.connect_to_local(
    host="localhost",  # Replace with your Weaviate Cloud URL
    port=8080,
    grpc_port=50051
)

imageObject = client.collections.get("ImageObject")

def get_entry_by_uuid(entry_uuid):
    """Retrieve an entry from Weaviate by its UUID and save the details to a JSON file."""
    try:
        data_object = imageObject.query.fetch_object_by_id(
            entry_uuid,
            include_vector=True
        )
        output_object = {
            "image_url": data_object.properties["image_url"],
            "vector": data_object.vector["default"]
        }
        with open('entry.json', 'w') as json_file:
            json.dump(output_object, json_file, indent=2)
        print("Entry saved to entry.json")
    except weaviate.exceptions.ObjectNotFoundException:
        print(f"Entry with UUID {entry_uuid} not found.")
    except Exception as e:
        print(f"Failed to retrieve entry. Error: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Retrieve a Weaviate entry by UUID.')
    parser.add_argument('--uuid', type=str, required=True, help='The UUID of the entry to retrieve.')
    args = parser.parse_args()

    get_entry_by_uuid(args.uuid)
    client.close()