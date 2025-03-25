from fastapi import FastAPI
from contextlib import asynccontextmanager

# Импортируем роутеры (пока пусто, добавим позже)
# from app.api.v1.api import api_router
# from app.core.config import settings

# Менеджер контекста для событий startup и shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Код, выполняемый при старте приложения
    print("Приложение запускается...")
    # Тут можно инициализировать соединения с БД, кэшем и т.д.
    yield
    # Код, выполняемый при остановке приложения
    print("Приложение останавливается...")
    # Тут можно закрыть соединения

# Создаем экземпляр FastAPI приложения
app = FastAPI(
    title="Tron Address Info Service",
    description="Микросервис для получения информации по адресу Tron и логирования запросов.",
    version="0.1.0",
    lifespan=lifespan # Добавляем менеджер контекста
)

# Подключаем роутеры API (раскомментировать позже)
# app.include_router(api_router, prefix=settings.API_V1_STR)

# Базовый эндпоинт для проверки работоспособности
@app.get("/", tags=["Health Check"])
async def root():
    """
    Проверка работоспособности сервиса.
    """
    return {"message": "Сервис работает"}

# Запуск приложения для локальной разработки
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)