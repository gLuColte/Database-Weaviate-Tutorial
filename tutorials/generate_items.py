
######################################################################
# post_entry.py
# Completed: 23/11/2024
# Author: Gary Lu
# Description: This script creates and insert entries in Weaviate one by one.
######################################################################  
import uuid
import random
from faker import Faker

######################################################################
# Functions
######################################################################
def generate_random_vector(size):
    """Generate a random vector with 'size' dimensions."""
    return [random.random() for _ in range(size)]

def generate_similar_vector(baseVector, variation=0.1):
    """Generate a vector similar to the base vector with slight variations."""
    return [value + random.uniform(-variation, variation) for value in baseVector]

def generate_item_properties(properties, vectorSize, baseVector=None):
    """Generate a random value for each property."""
    itemProperties = {}
    uuidValue = str(uuid.uuid4())

    def handle_image_url():
        return f"http://example.com/image_{uuidValue}.jpg"

    def handle_uuid():
        return uuidValue

    def handle_similarity_vector():
        return generate_similar_vector(baseVector) if baseVector is not None else generate_random_vector(vectorSize)
    
    def handle_random_test():
        fake = Faker()
        # Return random generated string
        return fake.sentence(nb_words=10)
    
    def handle_description():
        fake = Faker()
        # Return random generated string
        return fake.sentence(nb_words=20)

    # Define the switch dictionary
    switch = {
        "imageUrl": handle_image_url,
        "uuid": handle_uuid,
        "similarityVector": handle_similarity_vector,
        "randomTest": handle_random_test,
        "description": handle_description
    }

    for property in properties:
        propertyName = property["name"]
        if propertyName in switch:
            # Call the appropriate handler
            itemProperties[propertyName] = switch[propertyName]()
        else:
            raise ValueError(f"Property {propertyName} not expected.")

    return itemProperties