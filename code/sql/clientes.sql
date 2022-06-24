DROP TABLE IF NOT EXISTS clientes;

CREATE TABLE clientes(
    id_clientes     INTEGER     PRIMARY KEY     AUTOINCREMENT,
    nombre          VARCHAR(50) NOT NULL,
    email           VARCHAR(50) NOT NULL
    );

INSERT INTO clientes (nombre,email) VALUES
("Rodrigo","rodri@email.com"),
("David","david@email.com"),
("Karen","karen@email.com");

.headers ON

SELECT * FROM clientes;


