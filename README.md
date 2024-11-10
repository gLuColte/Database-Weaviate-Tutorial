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

### Weaviate Installation
Follow the steps in the Weaviate documentation for installing Weaviate via Docker Compose.

Here’s a simple Docker Compose setup for Weaviate:
```terminal
version: '3.7'
services:
  weaviate:
    image: semitechnologies/weaviate:latest
    container_name: weaviate
    environment:
      - QUERY_DEFAULTS=10
      - AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED=true
      - WEAVIATE_LOG_LEVEL=info
    ports:
      - "8080:8080"
    restart: always
```
