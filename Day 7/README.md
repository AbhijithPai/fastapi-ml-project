# Day 7 – Observability Foundations (MLOps)
Time taken: 3 hours

## What I Worked On
Today’s focus was on adding **basic observability** to the Sentiment Analysis API without overengineering, keeping it production-aligned and lightweight.

## Key Implementations

### 1. Request-Level Logging (Middleware)
- Implemented a FastAPI **HTTP middleware** to log every request.
- Captured:
  - HTTP method
  - API path
  - Response status code
  - Latency (ms)
  - Unique request identifier (`request_id`)

### 2. Request ID Propagation
- Generated a **UUID-based `request_id`** per request.
- Stored it in `request.state.request_id`.
- Returned it to clients via the `X-Request-ID` response header.
- Propagated the same `request_id` into model predictions.

### 3. Model-Level Traceability
- Updated sentiment model interfaces to accept `request_id`.
- Ensured predictions include:
  - model version
  - sentiment output
  - confidence score
  - request identifier

### 4. Error-Aware Logging
- Middleware logs structured error messages with:
  - request_id
  - API path
  - failure reason
- Enables fast root-cause analysis.

## Why This Matters
- Enables **debugging across services**
- Supports **traceability in production**
- Forms the foundation for:
  - metrics
  - distributed tracing
  - monitoring dashboards later

## Tech Stack
- FastAPI
- Transformers (Hugging Face)
- Custom middleware
- Structured logging

## Status
✅ Observability (foundation) completed  
➡ Next: environment-driven configs, caching, then LLMOps

