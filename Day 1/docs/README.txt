# Day 1: FastAPI Sentiment Analysis API

**Date:** 4th Dec 2025  
**Time spent:** ~3 hours  

## Objectives:
- Learn FastAPI basics
- Deploy a simple ML model (Linear Regression)
- Extend API for sentiment analysis using HuggingFace pipeline

## Work Done:
1. Created a Linear Regression model and saved it as `model.pkl`.
2. Built a FastAPI POST endpoint `/predict` to serve ML predictions.
3. Tested API using Swagger docs (`http://127.0.0.1:8000/docs`).
4. Added HuggingFace sentiment analysis pipeline to FastAPI:
   - Handled input via Pydantic model
   - Tested online
   - Ensured proper caching of model
5. Debugged common issues:
   - Field name mismatch in JSON
   - Internal Server Error handling
   - Local vs online model loading

## Observations:
- Linear regression API works perfectly for numeric predictions.
- Sentiment analysis API returns correct labels (POSITIVE/NEGATIVE) with high confidence scores.
- Score variation is small for simple sentences (expected behavior).

## Next Steps:
- Add more robust error handling to endpoints
- Integrate nuanced sentiment scoring
- Start experimenting with multiple ML/LLM endpoints in the same API
- Deploy API to cloud (Heroku / AWS / GCP)

**Link to repo:** [Your GitHub Repo](#)
