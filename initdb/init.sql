CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    date DATE,
);

INSERT INTO tasks (title, description, date) 
VALUES 
('Aprender Flask', 'Primer paso para dominar backend en Python', '2025-02-15'),
('Hacer un CRUD', 'Implementar las operaciones básicas para tareas', '2025-02-15');

