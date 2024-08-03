import os


APP_DEBUG_MODE: bool = os.getenv("APP_DEBUG_MODE", "True").lower() in ("true", "t", "1")
DATABASE_HOST: str = os.getenv("POSTGRES_HOST")
DATABASE_NAME: str = os.getenv("POSTGRES_DB")
DATABASE_PORT: int = os.getenv("POSTGRES_PORT")
DATABASE_USER: str = os.getenv("POSTGRES_USER")
DATABASE_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
