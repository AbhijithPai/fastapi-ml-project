# Day 3: Pydantic Validation & Model Versioning

**Date:** 5th Dec 2025  
**Time spent:** ~3 hours  

## Objectives:
- Implement input validation using **Pydantic** in FastAPI to make APIs robust.
- Introduce **model versioning** for managing multiple ML model iterations.
- Ensure the API is **production-ready** and maintainable for future enhancements.

## Work Done:
1. **Implemented Pydantic Models for Input Validation**
   - Created structured request models to enforce type safety.
   - Ensured API rejects invalid or malformed inputs automatically.
   - Example:
   ```python
   from pydantic import BaseModel

   class NumberInput(BaseModel):
       value: float

