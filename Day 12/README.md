# Day 12 - LLMOps Journey

Time: 2 hours

## Overview
Start of **LLMOps** after completing MLOps. Today’s goal: run a **small local LLM** for inference without heavy dependencies or login.

## Theory
- **LLMOps**: managing, deploying, monitoring large language models in production.
- Extends MLOps principles:
  - Large model sizes
  - Resource management (CPU/GPU)
  - Versioning & updates
  - Efficient inference pipelines
- Today: use a **minimal local LLM** to avoid heavy installs.

## Tools & Libraries
- Python 3.13  
- [ctransformers](https://pypi.org/project/ctransformers/)  
- FastAPI + Uvicorn  
- No Torch, No Transformers, No HuggingFace login  

