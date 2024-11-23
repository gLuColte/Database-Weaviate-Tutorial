######################################################################
# post_entries.py
# Completed: 23/11/2024
# Author: Gary Lu
# Description: This script creates and insert entries in Weaviate in batch.
######################################################################  

import os
import json
import random
import datetime
import argparse
import weaviate
from dotenv import load_dotenv

######################################################################
# Load environment variables
######################################################################
# Load environment variables from .env file
load_dotenv('../.env')

parser = argparse.ArgumentParser(description='Create entries in Weaviate.')
parser.add_argument('--collectionName', type=str, required=True, help='The name of the collection to create entries in.')
parser.add_argument('--outputJson', type=str, default="entry.json", help='The path to the entry JSON file.')
parser.add_argument('--uuid', type=str, help='The UUID of the entry to retrieve.')

# Parse the arguments
args = parser.parse_args()

# TIME FORMAT
TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f%z"

######################################################################
# Functions
######################################################################

def get_entry_uuids_in_collection(collectionClient):
    """Retrieve an entry from Weaviate by its UUID and save the details to a JSON file."""
    return [_.uuid for _ in collectionClient.iterator()]

def get_entry_by_uuid(collectionClient, entryUuid, filePath=None):
    """Retrieve an entry from Weaviate by its UUID and save the details to a JSON file."""
    try:
        rawObject = collectionClient.query.fetch_object_by_id(
            entryUuid,
            include_vector=True
        )
        # Iterate
        dataObject = {}
        for key, value in rawObject.properties.items():
            dataObject[key] = value
        # Get Metadata
        # Where creation_time=datetime.datetime(2024, 11, 23, 4, 35, 41, 399000, tzinfo=datetime.timezone.utc), last_update_time=datetime.datetime(2024, 11, 23, 4, 35, 41, 399000, tzinfo=datetime.timezone.utc)
        dataObject["metadata"] = {
            # Convert to using datetime.datetime.strptime   
            "creation_time": datetime.datetime.strftime(rawObject.metadata.creation_time, TIME_FORMAT),
            "last_update_time": datetime.datetime.strftime(rawObject.metadata.last_update_time, TIME_FORMAT)
        }
        # Get Vector
        dataObject["vector"] = rawObject.vector["default"]
        if filePath:
            with open(filePath, 'w') as json_file:
                json.dump(dataObject, json_file, indent=2)
            print(f"Entry saved to {filePath}")
        else:
            return dataObject
    except weaviate.exceptions.ObjectNotFoundException:
        print(f"Entry with UUID {entryUuid} not found.")
    except Exception as e:
        print(f"Failed to retrieve entry. Error: {str(e)}")

######################################################################
# Main
######################################################################
if __name__ == "__main__":
    # Retrieve environment variables
    host = os.getenv("WEAVIATE_HOST", "localhost")
    port = int(os.getenv("WEAVIATE_PORT", 8080))
    grpcPort = int(os.getenv("WEAVIATE_GRPC_PORT", 50051))

    # Connect to Weaviate
    client = weaviate.connect_to_local(
        host=host,
        port=port,
        grpc_port=grpcPort
    )
    
    # Get collection client
    collectionClient = client.collections.get(args.collectionName)

    # If uuid is not provided, get all uuids in collection
    if not args.uuid:
        print("No UUID provided, selecting randomly from the collection.")
        # Select randomly from the list
        args.uuid = random.choice(get_entry_uuids_in_collection(collectionClient))
        print(f"Selected UUID: {args.uuid}")

    # Get
    get_entry_by_uuid(collectionClient, args.uuid, args.outputJson)
    
    # Close
    client.close()