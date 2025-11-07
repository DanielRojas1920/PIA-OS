CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL
);
INSERT INTO tasks (title) VALUES ('Aprender Flask'), ('Hacer un CRUD');
