from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = "127.0.0.1"
    server_port: int = 8000
    database_url: str = "postgresql+psycopg2://postgres:1@172.17.0.2/postgres"


settings = Settings(
    _env_file=".env",
    _env_file_encoding="utf-8"
)
