from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.logging.config import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    # App Startup
    setup_logging()
    yield


app = FastAPI(lifespan=lifespan)
