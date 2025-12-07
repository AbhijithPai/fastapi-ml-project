# Sentiment Analysis API (MLOps Day 5)

A simple, production-ready Sentiment Analysis REST API built using FastAPI and Hugging Face Transformers. This project follows clean MLOps practices with a reusable folder structure, Docker support, and API testing via Swagger UI.

## Day 5 Summary (3 Hours)

- Restructured the project into a reusable `app/`-based architecture
- Separated API routes, services, configuration, and utilities
- Integrated Hugging Face sentiment-analysis pipeline
- Implemented lazy model loading for efficiency
- Dockerized the application
- Cleaned unused Docker containers and dependencies
- Verified API functionality using Swagger UI

## Project Structure

.
├── app/
│   ├── api/
│   ├── core/
│   ├── services/
│   ├── utils/
│   └── main.py
├── Dockerfile
├── requirements.txt
└── README.md

## Tech Stack

- Python
- FastAPI
- Hugging Face Transformers
- Docker

## Running the Application

Local:
pip install -r requirements.txt  
uvicorn app.main:app --reload  

Docker:
docker build -t sentiment-api .  
docker run -p 8000:8000 sentiment-api  

Swagger UI:
http://localhost:8000/docs

## Author

Built as part of a structured MLOps learning roadmap  
Day 5 completed with ~3 hours of focused work

