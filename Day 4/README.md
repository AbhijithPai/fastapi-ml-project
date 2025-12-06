Day 4: FastAPI Middleware & Docker Containerization
Date: 6th Dec 2025
Time spent: ~3–4 hours

Objectives:

Understand and implement middleware in FastAPI.

Learn the basics of Docker and containerize a FastAPI application.

Run the API inside a container to ensure portability and consistency.

Understand the difference between application logic and deployment concerns.

Work Done:
Implemented FastAPI Middleware

Added middleware to run logic before and after each API request.

Used middleware for request logging and understanding request lifecycle.

Learned that middleware enhances behavior without changing endpoint outputs.

Example:

from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Request processed in {process_time:.4f}s")
    return response

Dockerized FastAPI Application

Created a Dockerfile to package the FastAPI app with dependencies.

Understood the role of WORKDIR as an internal container directory.

Exposed port 8000 and mapped it to the host machine.

Successfully ran the API using Docker instead of local Python.

Example Dockerfile:

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "analyze_text:app", "--host", "0.0.0.0", "--port", "8000"]

Key Learnings:

Middleware improves structure, logging, and request handling.

Docker ensures the app runs consistently across environments.

Application output remains the same, but execution context changes.

Production readiness focuses on reliability, not feature changes.

Challenges Faced:

ASGI app loading errors due to incorrect module path.

Confusion around WORKDIR, clarified as container-only path.

Docker and WSL integration issues on Windows.
