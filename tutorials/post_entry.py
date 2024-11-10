import weaviate
import random
import uuid
import os

client = weaviate.connect_to_local(
    host="localhost",  # Replace with your Weaviate Cloud URL
    port=8080,
    grpc_port=50051
)

imageObject = client.collections.get("ImageObject")

def generate_random_vector(size):
    """Generate a random vector with 'size' dimensions."""
    return [random.random() for _ in range(size)]

def generate_similar_vector(base_vector, variation=0.1):
    """Generate a vector similar to the base vector with slight variations."""
    return [value + random.uniform(-variation, variation) for value in base_vector]

def post_image_object(category_similarity):
    generated_uuid = str(uuid.uuid4())
    image_url = f"http://example.com/image_{generated_uuid}.jpg"
    data_object = {
        "image_url": image_url
    }
    inserted_uuid = imageObject.data.insert(
        uuid=generated_uuid,
        properties=data_object,
        vector=category_similarity
    )
    
    print(f"Successfully posted image object with UUID {inserted_uuid}.")

if __name__ == "__main__":
    num_items = 1000  # Number of items to create
    vector_size = 256  # Assuming the vector size is 256
    use_similar_vectors = True  # Set this flag to True to use similar vectors

    # Base vector for generating similar vectors
    base_vector = generate_random_vector(vector_size)

    for i in range(num_items):        
        if use_similar_vectors:
            category_similarity = generate_similar_vector(base_vector)
        else:
            category_similarity = generate_random_vector(vector_size)
        
        post_image_object(category_similarity)

client.close()