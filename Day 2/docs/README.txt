# 📘 Day 2 – FastAPI Logging + Error Handling + Modular ML API

**Date:** 4th Dec 2025  
**Time Spent:** ~2 hours  

---

## 🎯 Objectives for Day 2
- Add a proper logging system to FastAPI  
- Implement clean error handling  
- Split code into modular folders (models, utils)  
- Understand how production-style MLOps backend services are structured  
- Test all functionality using Swagger  

---

## 🛠 Work Done Today

### ✅ 1. Created a Logger Utility (`utils/logger.py`)
- Added timestamped logs  
- Added INFO + ERROR level logging  
- Prevented duplicate handlers  
- Tested logs using both endpoints  
- Verified that logs print correctly to terminal

### Example Log Output:
```
2025-12-05 14:10:22 - INFO - User gave input: 10
```

---

### ✅ 2. Updated FastAPI App (`main.py`)
- Integrated logger into endpoints  
- Logged all incoming user data  
- Added safer function calls for ML logic  
- Imported functions properly from `models/` and `utils/`  

Endpoints updated:
- `/predict`  
- `/sentiment`  

Both now log:
- Inputs  
- Errors (if any)  

---

### ✅ 3. Implemented Error Handling
Inside model functions:
- Wrapped all processing inside `try-except`  
- Used `logger.error()` to log exceptions  
- Returned clean responses instead of crashes

Example failed input:
```
{ "value": "abc" }
```

Results in:
```
{"detail": "Internal Server Error"}
```
And terminal logs show exact error reason.

---

### ✅ 4. Organized Project Structure

```
project/
│── main.py
│── models/
│     ├── regression.py
│     ├── sentimentanalysis.py
│── utils/
│     ├── logger.py
│── requirements.txt
```

- `models/` contains all ML logic  
- `utils/logger.py` contains shared logging  
- `main.py` contains endpoints only (clean separation)

---

## 🧪 Testing Done
- Swagger URL: `http://127.0.0.1:8000/docs`  
- Tested numeric prediction → logs printed  
- Tested sentiment analysis → logs printed  
- Triggered errors using wrong input → error logs printed  
- Verified endpoints behave cleanly with error handling  

---

## 📌 Observations
- Logging is NOT visible in Swagger — only in terminal  
- Import names must match exactly (`get_logging` vs `get_logger`)  
- Error handling prevents API crashes  
- Project is now structured like real MLOps microservices  
- Logging is extremely useful for debugging input issues  

---

## 🚀 Next Steps (Day 3 Preview)
- Add **file-based logging** (`logs/app.log`)  
- Add **unit tests** using pytest  
- Create Dockerfile  
- Add environment-based config  
- Add small text-analysis endpoint (sentence length + contains “Abhi”)  

---

## 📎 Repo Link
(Add your GitHub repo link here)

---

