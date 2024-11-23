######################################################################
# post_collection.py
# Completed: 23/11/2024
# Author: Gary Lu
# Description: This script creates collections in Weaviate based on the configuration provided in a JSONC file.
######################################################################  
import os
import argparse
import weaviate
import commentjson
from dotenv import load_dotenv
from weaviate.classes.config import Property, DataType, Configure

######################################################################
# Load environment variables
######################################################################

# Load environment variables from .env file
load_dotenv('../.env')

# Parse Setup
parser = argparse.ArgumentParser(description='Create a collection in Weaviate.')
parser.add_argument('--configurationJsonc', type=str, default="collectionConfig.jsonc", help='The path to the configuration JSONC file.')

# Parse the arguments
args = parser.parse_args()

# DataType Mapping
WEAVIATE_DATA_TYPE_MAPPING = {
    "text": DataType.TEXT,
    "numberArray": DataType.NUMBER_ARRAY,
    "text": DataType.TEXT
}

######################################################################
# Functions
######################################################################

def create_collection(collectionName, properties, vectorizerConfig=None):
    """Create a collection in Weaviate."""
    client.collections.create(
        name = collectionName,
        properties = properties,
        vectorizer_config = vectorizerConfig if vectorizerConfig is not None else Configure.Vectorizer.none()
    )
    print(f"Successfully created {collectionName} collection in Weaviate.")

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

    # Read and parse the JSONC file
    with open(args.configurationJsonc, "r") as file:
        configuration = commentjson.load(file)

    # Check connection
    if client.is_ready():
        print("Connected to Weaviate successfully.")
        for collectionName, collectionConfiguration in configuration.items():
            properties = [Property(name=property["name"], data_type=WEAVIATE_DATA_TYPE_MAPPING[property["dataType"]]) for property in collectionConfiguration["properties"] if property["name"] not in ["uuid", "similarityVector"]]
            create_collection(collectionName, properties)
    else:
        print("Failed to connect to Weaviate.")

    client.close()