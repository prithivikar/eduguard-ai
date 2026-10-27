import os
from pydantic import BaseModel

def get_database_url() -> str:
    db_url = os.getenv("DATABASE_URL")
    if db_url:
        if db_url.startswith("postgres://"):
            db_url = db_url.replace("postgres://", "postgresql://", 1)
        return db_url
    default_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "eduguard.db")
    return f"sqlite:///{default_path}"

class Settings(BaseModel):
    PROJECT_NAME: str = "EduGuard AI"
    VERSION: str = "1.0.0"
    API_V1_PREFIX: str = "/api"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "eduguard_ai_super_secret_jwt_key_2026_hackathon")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    
    DB_PATH: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "eduguard.db")
    DATABASE_URL: str = get_database_url()

settings = Settings()
