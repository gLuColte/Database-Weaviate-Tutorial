import weaviate
import random
import os
import uuid
from weaviate.util import generate_uuid5
import weaviate.classes as wvc

# Initialize the Weaviate client
client = weaviate.connect_to_local(
    host="localhost",  # Replace with your Weaviate Cloud URL
    port=8080,
    grpc_port=50051
)
def generate_random_vector(size):
    """Generate a random vector with 'size' dimensions."""
    return [random.random() for _ in range(size)]

def generate_similar_vector(base_vector, variation=0.1):
    """Generate a vector similar to the base vector with slight variations."""
    return [value + random.uniform(-variation, variation) for value in base_vector]

if __name__ == "__main__":
    num_items = 1000  # Number of items to create
    vector_size = 256  # Assuming the vector size is 256
    use_similar_vectors = True  # Set this flag to True to use similar vectors

    # Base vector for generating similar vectors
    base_vector = generate_random_vector(vector_size)

    data_objects = []

    for i in range(num_items):
        # Generate a UUID for both the image URL and the data object
        generated_uuid = str(uuid.uuid4())
        image_url = f"http://example.com/image_{generated_uuid}.jpg"
        
        if use_similar_vectors:
            category_similarity = generate_similar_vector(base_vector)
        else:
            category_similarity = generate_random_vector(vector_size)
        
        data_object = wvc.data.DataObject(
            uuid=generated_uuid,
            properties={
                "image_url": image_url
            },
            vector=category_similarity
        )
        
        data_objects.append(data_object)

    # Insert all data objects at once
    response = client.collections.get("ImageObject").data.insert_many(data_objects)
    print("Successfully inserted data objects.")

client.close()