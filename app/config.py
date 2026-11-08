import os
from urllib.parse import quote_plus
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

# Автоматически определяем путь к секретам: в Docker это /run/secrets, локально — папка secrets
default_secrets_dir = "/run/secrets" if os.path.exists("/run/secrets") else "secrets"

class Settings(BaseSettings):
    app_name: str = "Cloud Application"
    app_version: str = "1.0"
    app_description: str = "Учебное серверное приложение для облачных систем."
    app_env: str = "development"
    app_host: str = "127.0.0.1"
    app_port: int = 8000
    debug: bool = True

    # База данных
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "cloud_db"  # Должно совпадать с POSTGRES_DB в compose.yaml
    db_user: str = "postgres"
    lab_db_password: SecretStr
    auth_secret: SecretStr

    # Хранилище объектов
    storage_path: str = "storage/objects"

    # Параметры интеграции с Notification Service
    notification_service_url: str = "http://localhost:9000"
    notification_timeout_seconds: float = 3.0
    notification_max_attempts: int = 3
    notification_retry_delay_seconds: float = 0.5

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        secrets_dir=default_secrets_dir,
        extra="ignore"
    )

    @property
    def database_url(self) -> str:
        password = quote_plus(self.lab_db_password.get_secret_value())
        return (
            "postgresql+psycopg2://"
            f"{self.db_user}:"
            f"{password}@"
            f"{self.db_host}:"
            f"{self.db_port}/"
            f"{self.db_name}"
        )

settings = Settings()