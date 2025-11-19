CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO tasks (title, description) 
VALUES 
('Aprender Flask', 'Primer paso para dominar backend en Python'),
('Hacer un CRUD', 'Implementar las operaciones básicas para tareas');
