-- Выборка всех сервисов
SELECT * FROM services;

-- Фильтрация по статусу
SELECT * FROM services WHERE status = 'running';

-- Получение сервисов с наименованием типа через JOIN
SELECT
    services.id,
    services.name,
    service_types.name AS type,
    services.status
FROM services
JOIN service_types ON services.type_id = service_types.id
ORDER BY services.id;

-- Обновление статуса
UPDATE services SET status = 'running' WHERE id = 3;

-- Выборка по конкретному ID
SELECT * FROM services WHERE id = 1;