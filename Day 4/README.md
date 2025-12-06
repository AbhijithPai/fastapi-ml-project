# Day 4: FastAPI Middleware & Docker Containerization

# Date
6th Dec 2025

# Time Spent
~3–4 hours

# Objectives
- Implement middleware in FastAPI to understand the request–response lifecycle
- Learn Docker fundamentals and containerize a FastAPI application
- Run the API inside a container for portability and consistency
- Separate application logic from deployment concerns

# Work Done

## Implemented FastAPI Middleware
- Added middleware to execute code before and after each API request
- Used middleware for logging request processing time
- Ensured core endpoint logic remained unchanged

## Example
```python
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
