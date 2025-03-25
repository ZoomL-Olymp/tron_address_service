import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

class Settings(BaseSettings):
    """
    Класс для хранения настроек приложения.
    Значения по умолчанию берутся из переменных окружения.
    """
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost:5432/tron_default_db")
    # Можно добавить другие настройки сюда, например:
    # TRON_NODE_URI: str = os.getenv("TRON_NODE_URI", "https://api.trongrid.io")
    # API_V1_STR: str = "/api/v1" # Префикс для API v1

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

# Создаем экземпляр настроек, который будет использоваться в приложении
settings = Settings()

# Пример вывода для проверки при запуске модуля напрямую
if __name__ == "__main__":
    print("Загруженные настройки:")
    print(f"DATABASE_URL: {settings.DATABASE_URL}")
    # print(f"TRON_NODE_URI: {settings.TRON_NODE_URI}")