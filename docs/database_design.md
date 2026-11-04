# Проектирование базы данных Cloud Application

## 1. Назначение базы данных
База данных предназначена для постоянного хранения информации об облачных сервисах и их типах в приложении Cloud Application.

## 2. Сущности

### ServiceType (Тип облачного сервиса)
- `id` (INTEGER, PK) — уникальный идентификатор типа;
- `name` (VARCHAR(50)) — название типа (application, database, monitoring);
- `description` (VARCHAR(255)) — описание типа.

### Service (Облачный сервис)
- `id` (INTEGER, PK) — уникальный идентификатор сервиса;
- `name` (VARCHAR(100)) — название сервиса;
- `type_id` (INTEGER, FK -> ServiceType.id) — ссылка на тип сервиса;
- `status` (VARCHAR(20)) — текущее состояние сервиса (`running`, `maintenance`, `stopped`).

## 3. Связи
- Связь между `ServiceType` и `Service`: **1 : N** (один тип может использоваться множеством сервисов, но каждый сервис принадлежит только одному типу).

## 4. Логическая модель
SERVICE_TYPES

PK  id           INTEGER
name         VARCHAR(50)
description  VARCHAR(255)
SERVICES

PK  id           INTEGER
name         VARCHAR(100)
FK  type_id      INTEGER  --> SERVICE_TYPES.id
status       VARCHAR(20)
## 5. Ограничения целостности
1. `Service.id` и `ServiceType.id` уникальны (Primary Key).
2. `Service.type_id` должен ссылаться на существующую запись в `ServiceType` (Foreign Key).
3. `Service.status` принимает только допустимые значения: `running`, `maintenance`, `stopped`.
4. `Service.name` и `ServiceType.name` являются обязательными полями (NOT NULL).