import requests
import json
import random
import uuid

# Weaviate server URL
WEAVIATE_URL = "http://localhost:8080/v1/objects"

def generate_random_vector(size):
    """Generate a random vector with 'size' dimensions."""
    return [random.random() for _ in range(size)]

def generate_similar_vector(base_vector, variation=0.1):
    """Generate a vector similar to the base vector with slight variations."""
    return [value + random.uniform(-variation, variation) for value in base_vector]

def post_image_object(category_similarity):
    uuidStr = str(uuid.uuid4())
    data_object = {
        "class": "ImageObject",
        "properties": {
            "image_url": f"http://example.com/image_{uuidStr}.jpg",
            "category_similarity": category_similarity,
            "uuid": uuidStr
        }
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(WEAVIATE_URL, headers=headers, data=json.dumps(data_object))
    
    if response.status_code == 200:
        print(f"Successfully posted image object with UUID {data_object['properties']['uuid']}.")
    else:
        print(f"Failed to post image object. Status code: {response.status_code}")
        print("Response:", response.text)

if __name__ == "__main__":
    num_items = 10000  # Number of items to create
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