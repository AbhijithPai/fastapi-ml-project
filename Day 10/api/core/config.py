import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    ENV = os.getenv("ENV", "development")
    MODEL_VERSION = os.getenv("MODEL_VERSION", "v1")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()
