######################################################################
# get_similar_entries.py
# Completed: 23/11/2024
# Author: Gary Lu
# Description: This script retrieves similar entries from Weaviate by its UUID.
######################################################################  
import os
import uuid
import random
import json
import pandas as pd
import argparse
import weaviate
import commentjson
from dotenv import load_dotenv
from weaviate.classes.query import MetadataQuery
######################################################################
# Load environment variables
######################################################################
# Load environment variables from .env file
load_dotenv('../.env')


parser = argparse.ArgumentParser(description='Retrieve similar entries from Weaviate by its UUID.')
parser.add_argument('--inputJson', type=str, default="entry.json", help='The path to the entry JSON file.')
parser.add_argument('--configurationJsonc', type=str, default="collectionConfig.jsonc", help='The path to the configuration JSONC file.')
parser.add_argument('--distance', type=float, default=0.009, help='The distance threshold for similar entries.')
parser.add_argument('--limit', type=int, default=50, help='The maximum number of similar entries to retrieve.')
parser.add_argument('--outputCsv', type=str, default="similar_entries.csv", help='The path to the output CSV file.')
# Parse the arguments
args = parser.parse_args()

######################################################################
# Functions
######################################################################

def get_similar_entries(weaviateClient, entry, configuration, distance, limit):
    # Client
    collectionClient = weaviateClient.collections.get(entry["collectionName"]) 
    
    # Get Configuration
    collectionConfiguration = configuration[entry["collectionName"]]
    
    # Query using collectionClient
    response = collectionClient.query.near_vector(
        near_vector=entry["vector"],
        distance=args.distance,
        limit=args.limit,
        return_metadata=MetadataQuery(distance=True)
    )
    
    # Iterate through the response
    results = []
    for object in response.objects:
        result = {}
        for property in collectionConfiguration["properties"]:
            # If it is similarityVector, ignore
            if property["name"] == "similarityVector":
                continue    
            result[property["name"]] = object.properties.get(property["name"])
        result["distance"] = object.metadata.distance
        result["uuid"] = object.uuid
        results.append(result)
    
    # Convert the list of dictionaries to a DataFrame
    return pd.DataFrame(results)

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
    
    # Read the entry from the JSON file
    with open(args.inputJson, 'r') as json_file:
        entry = json.load(json_file)
    
    # Collection Configuration 
    with open(args.configurationJsonc, "r") as file:
        configuration = commentjson.load(file)
    
    # Get similar entries
    resultDf = get_similar_entries(client, entry, configuration, args.distance, args.limit)

    # Save to CSV
    resultDf.to_csv(args.outputCsv, index=False)

    client.close()