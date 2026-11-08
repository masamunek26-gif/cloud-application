INSERT INTO service_types (name, description)
VALUES
    ('application', 'Прикладной сервис'),
    ('database', 'Сервис хранения данных'),
    ('monitoring', 'Сервис мониторинга');

INSERT INTO services (name, type_id, status)
VALUES
    ('Web Service', 1, 'running'),
    ('Database Service', 2, 'running'),
    ('Monitoring Service', 3, 'maintenance');