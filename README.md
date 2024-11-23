![Main Banner](./markdown-images/main-banner.png)

# Database-Weaviate-Tutorial
Welcome to the Weaviate Mastery Repository! This repository is your guide to mastering Weaviate, an open-source vector database that enables the creation of semantic search engines and AI applications. You'll explore various operations like creating, reading, updating, and deleting (CRUD) data using Weaviate with Python, all while leveraging Weaviate's capabilities for vector search and machine learning integration.

## Why Learn Weaviate?
Weaviate is a powerful tool for modern data applications. Understanding Weaviate is important for several reasons:

1. **Vector Search**: Weaviate is designed to perform vector search, making it ideal for applications involving AI, natural language processing, and semantic search.
2. **Scalability**: Built to handle large-scale data, Weaviate offers horizontal scaling, making it a strong choice for production-grade applications.
3. **Schema-Free**: Unlike traditional relational databases, Weaviate allows you to store and query data with flexible schemas that support dynamic structures.
4. **Integration with Machine Learning**: Weaviate integrates seamlessly with machine learning models, enabling you to enhance your search engine with semantic understanding.
5. **Advanced Queries**: With Weaviate's GraphQL interface, you can perform complex queries that are not only fast but also contextually relevant.

## Weaviate vs. Other Databases
While traditional relational databases like MySQL or NoSQL databases like MongoDB have their strengths, Weaviate stands out for its unique approach to:

- **Vector-Based Search**: Unlike traditional DBs, Weaviate allows searching and querying based on semantic vectors (e.g., using embeddings from AI models).
- **Horizontal Scalability**: Weaviate can scale across multiple nodes, making it suitable for distributed environments.
- **ML Integration**: Direct integration with machine learning models allows for enriched data analysis and semantic search capabilities.

## Dive Deep into Weaviate!
Weaviate provides an intuitive way to store and search data with machine learning-backed features. The aim of this repository is to introduce you to basic CRUD operations, empowering you to use Weaviate for real-world AI-driven applications.

## Setup

### Docker

Follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/) to install Docker Engine.

Please ensure to enable Non-Root User Access for Docker - [How to Fix Docker Permission Denied?](https://phoenixnap.com/kb/docker-permission-denied):
```terminal
sudo groupadd -f docker
sudo usermod -aG docker $USER
newgrp docker
```

### Docker Compose
Follow [Install the Compose plugin](https://docs.docker.com/compose/install/) to install Docker-Compose Plugin.
```
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

### Python Installation
Follow [Python Installation](https://www.python.org/downloads/) to install Python. Then install the required packages:

```terminal
pip install -r requirements.txt
```

### Weaviate Installation
Follow the steps in the Weaviate documentation for installing Weaviate via Docker Compose.

Here’s a simple Docker Compose setup for Weaviate:
```terminal
version: '3.7'
services:
  weaviate:
    image: cr.weaviate.io/semitechnologies/weaviate:1.27.2
    ports:
      - "8080:8080"
      - "50051:50051"
    environment:
      - PERSISTENCE_DATA_PATH=/var/lib/weaviate
    volumes:
      - ${WEAVIATE_DATA_PATH}:/var/lib/weaviate
    env_file:
      - .env
```

Weaviate UI is included in the docker-compose file for easier visualization.

## Tutorials

Start with configuring collectionConfig.jsonc in tutorials folder, which defines the schema of the collections.

### 1. Create Collections

Run the following command to create collections:
```terminal
$> python tutorials/post_collection.py -h
usage: post_collection.py [-h] [--configurationJsonc CONFIGURATIONJSONC]

Create a collection in Weaviate.

options:
  -h, --help            show this help message and exit
  --configurationJsonc CONFIGURATIONJSONC
                        The path to the configuration JSONC file.

```

### 2. Insert Entries

Run the following command to insert entries:
```terminal
$> python tutorials/post_entries.py -h
usage: post_entries.py [-h] [--configurationJsonc CONFIGURATIONJSONC] --collectionName COLLECTIONNAME [--numberOfItems NUMBEROFITEMS] [--vectorSize VECTORSIZE]
                       [--useSimilarVectors USESIMILARVECTORS]

Create entries in Weaviate.

options:
  -h, --help            show this help message and exit
  --configurationJsonc CONFIGURATIONJSONC
                        The path to the configuration JSONC file.
  --collectionName COLLECTIONNAME
                        The name of the collection to create entries in.
  --numberOfItems NUMBEROFITEMS
                        Number of items to create.
  --vectorSize VECTORSIZE
                        Size of the vector.
  --useSimilarVectors USESIMILARVECTORS
                        Flag to use similar vectors
```
Or use the following to insert one entry at a time:
```terminal
$> python tutorials/post_entry.py -h
usage: post_entry.py [-h] [--configurationJsonc CONFIGURATIONJSONC] --collectionName COLLECTIONNAME [--numberOfItems NUMBEROFITEMS] [--vectorSize VECTORSIZE]
                     [--useSimilarVectors USESIMILARVECTORS]

Create entries in Weaviate.

options:
  -h, --help            show this help message and exit
  --configurationJsonc CONFIGURATIONJSONC
                        The path to the configuration JSONC file.
  --collectionName COLLECTIONNAME
                        The name of the collection to create entries in.
  --numberOfItems NUMBEROFITEMS
                        Number of items to create.
  --vectorSize VECTORSIZE
                        Size of the vector.
  --useSimilarVectors USESIMILARVECTORS
                        Flag to use similar vectors
```

### 3. Get Single Entry

Run the following command to get a single entry:
```terminal
$> python tutorials/get_single_entry.py -h
usage: get_single_entry.py [-h] --collectionName COLLECTIONNAME [--outputJson OUTPUTJSON] [--uuid UUID]

Retrieve a single entry from Weaviate by its UUID.

options:
  -h, --help            show this help message and exit
  --collectionName COLLECTIONNAME
                        The name of the collection to retrieve the entry from.
  --outputJson OUTPUTJSON
                        The path to the entry JSON file.
  --uuid UUID           The UUID of the entry to retrieve.
```

This will generate an entry.json file in the folder.

### 4. Get Similar Entries

Run the following command to get similar entries:
```terminal
$> python tutorials/get_similar_entries.py -h
usage: get_similar_entries.py [-h] [--inputJson INPUTJSON] [--configurationJsonc CONFIGURATIONJSONC] [--distance DISTANCE] [--limit LIMIT] [--outputCsv OUTPUTCSV]

Retrieve similar entries from Weaviate by its UUID.

options:
  -h, --help            show this help message and exit
  --inputJson INPUTJSON
                        The path to the entry JSON file.
  --configurationJsonc CONFIGURATIONJSONC
                        The path to the configuration JSONC file.
  --distance DISTANCE   The distance threshold for similar entries.
  --limit LIMIT         The maximum number of similar entries to retrieve.
  --outputCsv OUTPUTCSV
                        The path to the output CSV file.
```

This will generate a similar_entries.csv file in the folder.