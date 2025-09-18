from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database.engine import setup_database
from app.logging.config import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    # App Startup
    setup_logging()
    await setup_database()
    yield


app = FastAPI(lifespan=lifespan)
