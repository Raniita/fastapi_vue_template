from src.config import settings

TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": [
            "src.database.models", "aerich.models"
            ],
            "default_connection": "default"
        } 
    }
}