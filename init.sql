CREATE TABLE ordenes(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Llave primaria',
    nombres_cliente VARCHAR(255),
    producto VARCHAR(255),
    cantidad int,
    email VARCHAR(255),
    direccion VARCHAR(255),
    fecha_creacion VARCHAR(255)

) COMMENT 'Tabla ordenes';