import weaviate

# Initialize the Weaviate client
client = weaviate.Client("http://localhost:8080", auth_client_secret=weaviate.AuthClientPassword("user1", "password1"))

# Define the schema for ImageObject
schema = {
    "classes": [
        {
            "class": "ImageObject",
            "description": "Stores images and their similarity matrices",
            "vectorIndexType": "hnsw",
            "vectorizer": "none",
            "properties": [
                {
                    "name": "image_url",
                    "dataType": ["string"],
                    "description": "URL of the image"
                },
                {
                    "name": "category_similarity",
                    "dataType": ["number[]"],
                    "description": "Similarity matrix for categories"
                },
                {
                    "name": "uuid",
                    "dataType": ["string"],
                    "description": "Unique identifier for the image object"
                }
            ]
        }
    ]
}

# Create the schema in Weaviate
client.schema.create(schema)

print("Successfully created ImageObject schema in Weaviate.")