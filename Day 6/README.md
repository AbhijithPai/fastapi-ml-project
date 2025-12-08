# Model Versioned Sentiment Analysis API

A FastAPI-based ML service demonstrating **model version control and system control**
without hardcoding logic or retraining complexity.

## Key Features
- Model versioning (v1, v2)
- Runtime model selection via query parameter
- Centralized model registry pattern
- Clean separation of API, system, and model logic
- Easy model upgrades and rollbacks without API changes

## Project Structure
.
├── api/
│   ├── routes.py
│   └── schema.py
├── core/
│   └── model_registry.py
├── models/
│   ├── v1.py
│   └── v2.py
├── main.py
└── README.md

## API Usage
POST /predict?version=v1  
POST /predict?version=v2  

Request:
{
  "text": "I love this product"
}

Response:
{
  "version": "v1",
  "label": "POSITIVE",
  "score": 0.89
}

## Core Concept
Models are managed using a **Model Registry** instead of if-else logic.
Models are loaded on demand, making the system scalable and production-ready.

## Learning Outcome
- Understanding model versioning in production
- Safe upgrades and rollbacks
- System-level thinking for ML services

Status: ✅ Model Version Control & System Control completed
Next: Observability (logging, metrics)

