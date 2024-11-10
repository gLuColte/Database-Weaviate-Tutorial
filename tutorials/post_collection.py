import weaviate
from weaviate.classes.config import Property, DataType, Configure
import os

import weaviate

client = weaviate.connect_to_local(
    host="localhost",  # Replace with your Weaviate Cloud URL
    port=8080,
    grpc_port=50051
)

# Check connection
if client.is_ready():
    print("Connected to Weaviate Cloud successfully.")

    # Define the collection for ImageObject
    image_object_collection = client.collections.create(
        name="ImageObject",
        properties=[
            Property(name="image_url", data_type=DataType.TEXT)
        ],
        vectorizer_config=Configure.Vectorizer.none()
    )

    print("Successfully created ImageObject collection in Weaviate.")
else:
    print("Failed to connect to Weaviate Cloud.")

client.close()