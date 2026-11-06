# Зависимости Cloud Application

## Прямые зависимости
- FastAPI — REST API
- Uvicorn — ASGI-сервер
- SQLAlchemy — ORM и доступ к БД
- Alembic — миграции
- psycopg2-binary — драйвер PostgreSQL
- pydantic-settings — конфигурация
- python-multipart — загрузка файлов
- pwdlib — хеширование паролей (Argon2)
- trustme — локальные TLS-сертификаты

## Установка и проверка
```powershell
python -m pip install -r requirements.txt
python -m pip check