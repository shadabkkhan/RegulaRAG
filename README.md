# RegulaRAG

RegulaRAG is a Retrieval Augmented Generation (RAG) application designed to answer questions about Indian financial regulations using source-grounded responses and citations.

## Planned Architecture

- **Frontend:** React
- **Backend API:** Java, Spring Boot, Spring Security
- **RAG Service:** Python, FastAPI
- **Database:** MySQL
- **Retrieval:** Vector search and BM25 hybrid retrieval
- **LLM:** Gemini

## Planned Features

- Ingest regulatory documents from official sources.
- Retrieve relevant document passages for user questions.
- Generate answers with source citations.
- Evaluate retrieval quality and answer faithfulness.
- Provide authentication and chat history.

## Project Structure

- backend/ - Spring Boot API
- rag-service/ - Python RAG service
- frontend/ - React application
- eval/ - Evaluation scripts and datasets
- data/ - Local regulatory document data
- docs/ - Project documentation

## Project Status

Initial setup. Features will be implemented incrementally and tested through separate Git branches and pull requests.
