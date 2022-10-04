from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise
import logging

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM
from src.config import settings

logger = logging.getLogger(__name__)

def create_app()-> FastAPI:
    app = FastAPI()

    # Enable logging
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()

    #formatter = logging.Formatter("%(asctime)s - %(module)s - %(funcName)s - line:%(lineno)d - %(levelname)s - %(message)s")
    formatter = logging.Formatter("%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s")

    ch.setFormatter(formatter)    
    logger.addHandler(ch)       # Exporting logs to stdout

    if settings.FILE_LOG:
        fh = logging.FileHandler(filename='./server.log')
        fh.setFormatter(formatter)
        logger.addHandler(fh)      # Exporting logs to file server.log
    
    logger.info("Logger UP!")
    logger.info(f"Logging to file: server.log --> {settings.FILE_LOG}")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:8080"],    # Endpoint Frontend
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    Tortoise.init_models(["src.database.models"], "models")
    
    from src.routes import users, notes

    app.include_router(users.router)
    app.include_router(notes.router)

    register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

    @app.get("/")
    async def home():
        return "Hello, World!"
    
    return app

app = create_app()