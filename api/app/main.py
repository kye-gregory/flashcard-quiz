from fastapi import FastAPI
from app.logging.config import setup_logging

setup_logging()
app = FastAPI()
