######################################################################
# post_entries.py
# Completed: 23/11/2024
# Author: Gary Lu
# Description: This script creates and insert entries in Weaviate in batch.
######################################################################  
import os
import uuid
import random
import argparse
import weaviate
from weaviate.classes.data import DataObject
import commentjson
from faker import Faker
from dotenv import load_dotenv
from generate_items import generate_random_vector, generate_similar_vector, generate_item_properties
######################################################################
# Load environment variables
######################################################################
# Load environment variables from .env file
load_dotenv('../.env')

# Parse Setup
parser = argparse.ArgumentParser(description='Create entries in Weaviate.')
parser.add_argument('--configurationJsonc', type=str, default="collectionConfig.jsonc", help='The path to the configuration JSONC file.')
parser.add_argument('--collectionName', type=str, required=True, help='The name of the collection to create entries in.')
parser.add_argument('--numberOfItems', type=int, default=1000, help='Number of items to create.')
parser.add_argument('--vectorSize', type=int, default=256, help='Size of the vector.')
parser.add_argument('--useSimilarVectors', type=bool, default=True, help='Flag to use similar vectors.')

# Parse the arguments
args = parser.parse_args()

######################################################################
# Functions
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
    
    # Read and parse the JSONC file
    with open(args.configurationJsonc, "r") as file:
        configuration = commentjson.load(file)

    # Check if collection name in Jsonc
    if args.collectionName not in configuration:
        raise ValueError(f"Collection name {args.collectionName} not found in the JSONC file.")

    # Read Properties from collection configuration
    properties = configuration[args.collectionName]["properties"]

    # Base vector for generating similar vectors
    baseVector = generate_random_vector(args.vectorSize)

    # Insert entries
    data_objects = []
    for i in range(args.numberOfItems):        
        itemProperties = generate_item_properties(properties, args.vectorSize, baseVector)
        data_objects.append(
            DataObject(
                uuid=itemProperties["uuid"],
                # Take out uuid/similarityVector
                properties={k: v for k, v in itemProperties.items() if k not in ["uuid", "similarityVector"]},
                vector=itemProperties["similarityVector"]
            )
        )
    response = collectionClient.data.insert_many(data_objects)
    print(f"Successfully posted {len(data_objects)} items through batch insert.")

    client.close()
