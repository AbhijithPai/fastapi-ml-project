import time
from fastapi import Request, HTTPException

last_called = {}

async def rate_limit(request: Request, call_next):
    client_ip = request.client.host
    current_time =  time.time()

    if client_ip in last_called:
        if current_time - last_called[client_ip] < 0.5:
            raise HTTPException(429, "Too many requests, slow down")
        
    last_called[client_ip] = current_time

    response = await call_next(request)

    return response