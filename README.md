# Customer Support System using RAG

## Overview
This project is a Customer Support System built using a Retrieval Augmented Generation (RAG) architecture.  
It retrieves relevant information from a knowledge base and generates accurate, context aware responses using a Large Language Model.

The system is implemented using a modular coding approach to keep the codebase clean, scalable, and production ready.

---

## Key Features
- RAG based question answering
- Vector database powered document retrieval
- Modular and maintainable code structure
- Environment variable based configuration
- API ready design using FastAPI

---

## Tech Stack
- Python
- LangChain
- AstraDB Vector Store
- FastAPI
- python-dotenv

---


## RAG Flow
1. Customer support data is ingested and processed
2. Data is converted into vector embeddings
3. Embeddings are stored in a vector database
4. User queries retrieve relevant documents
5. Retrieved context is passed to the LLM
6. Final response is generated using retrieved knowledge

---



