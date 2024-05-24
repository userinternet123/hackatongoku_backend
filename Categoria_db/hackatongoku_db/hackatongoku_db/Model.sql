
--DROP TABLE IF EXISTS TNotaRequerimiento;
--DROP TABLE IF EXISTS TTorneoCategoria;
--DROP TABLE IF EXISTS TCategoriaRequerimiento;
--DROP TABLE IF EXISTS TUser;
--DROP TABLE IF EXISTS TTorneo;
--DROP TABLE IF EXISTS TCategoria;

--DROP TABLE IF EXISTS TRequerimiento;
--DROP TABLE IF EXISTS Requerimiento;
--drop table if exists TluchadorTorneo;
--drop table if exists TPrueba;
select * from TUser
select * from TCategoria


CREATE TABLE TUser (
    id INT PRIMARY KEY IDENTITY,
    username NVARCHAR(255) NOT NULL,
    email NVARCHAR(255) NOT NULL,
    password NVARCHAR(255) NOT NULL,
    imagen VARCHAR(255),
    usuarioInserto NVARCHAR(255),
    fechaInserto DATETIME,
    usuarioModifico NVARCHAR(255),
    fechaModifico DATETIME,
    Eliminado BIT,
    Activo BIT
);

-- Tabla TTorneo
CREATE TABLE TTorneo (
    id INT PRIMARY KEY IDENTITY,
    anio INT NOT NULL,
    usuarioInserto NVARCHAR(255),
    fechaInserto DATETIME,
    usuarioModifico NVARCHAR(255),
    fechaModifico DATETIME,
    Eliminado BIT,
    Activo BIT
);

-- Tabla TCategoria
CREATE TABLE TCategoria (
    id INT PRIMARY KEY IDENTITY,
    nombre VARCHAR(100) NOT NULL,
    usuarioInserto NVARCHAR(255),
    fechaInserto DATETIME,
    usuarioModifico NVARCHAR(255),
    fechaModifico DATETIME,
    Eliminado BIT,
    Activo BIT
);

-- Tabla TRequerimiento
CREATE TABLE TRequerimiento (
    id INT PRIMARY KEY IDENTITY,
    descripcion VARCHAR(255) NOT NULL,
    usuarioInserto NVARCHAR(255),
    fechaInserto DATETIME,
    usuarioModifico NVARCHAR(255),
    fechaModifico DATETIME,
    Eliminado BIT,
    Activo BIT
);

-- Tabla Inscripción de Luchadores en Torneos
CREATE TABLE TInscripcion (
    id INT PRIMARY KEY IDENTITY,
    luchadorId INT,
    torneoId INT,
    ki DECIMAL(10, 2),
    esferas INT,
    usuarioInserto NVARCHAR(255),
    fechaInserto DATETIME,
    usuarioModifico NVARCHAR(255),
    fechaModifico DATETIME,
    Eliminado BIT,
    Activo BIT,
    FOREIGN KEY (luchadorId) REFERENCES TUser(id),
    FOREIGN KEY (torneoId) REFERENCES TTorneo(id)
);

-- Tabla para Registrar Notas de Requerimientos por Torneo y Luchador
CREATE TABLE TNotaRequerimiento (
    id INT PRIMARY KEY IDENTITY,
    requerimientoId INT,
    luchadorId INT,
    torneoId INT,
    nota DECIMAL(5, 2),
    usuarioInserto NVARCHAR(255),
    fechaInserto DATETIME,
    usuarioModifico NVARCHAR(255),
    fechaModifico DATETIME,
    Eliminado BIT,
    Activo BIT,
    FOREIGN KEY (requerimientoId) REFERENCES TRequerimiento(id),
    FOREIGN KEY (luchadorId) REFERENCES TUser(id),
    FOREIGN KEY (torneoId) REFERENCES TTorneo(id)
);

-- Tabla Relación Torneo - Categoría
CREATE TABLE TTorneoCategoria (
    id INT PRIMARY KEY IDENTITY,
    torneoId INT,
    categoriaId INT,
    usuarioInserto NVARCHAR(255),
    fechaInserto DATETIME,
    usuarioModifico NVARCHAR(255),
    fechaModifico DATETIME,
    Eliminado BIT,
    Activo BIT,
    FOREIGN KEY (torneoId) REFERENCES TTorneo(id),
    FOREIGN KEY (categoriaId) REFERENCES TCategoria(id)
);

-- Tabla Relación Categoría - Requerimiento
CREATE TABLE TCategoriaRequerimiento (
    id INT PRIMARY KEY IDENTITY,
    categoriaId INT,
    requerimientoId INT,
    usuarioInserto NVARCHAR(255),
    fechaInserto DATETIME,
    usuarioModifico NVARCHAR(255),
    fechaModifico DATETIME,
    Eliminado BIT,
    Activo BIT,
    FOREIGN KEY (categoriaId) REFERENCES TCategoria(id),
    FOREIGN KEY (requerimientoId) REFERENCES TRequerimiento(id)
);


-- Insertar Categorías
INSERT INTO TCategoria (nombre, usuarioInserto, fechaInserto, usuarioModifico, fechaModifico, Eliminado, Activo) 
VALUES 
('Base de Datos', 'admin', GETDATE(), 'admin', GETDATE(), 0, 1),
('Backend', 'admin', GETDATE(), 'admin', GETDATE(), 0, 1),
('Frontend', 'admin', GETDATE(), 'admin', GETDATE(), 0, 1);

-- Insertar Requerimientos
INSERT INTO TRequerimiento (descripcion, usuarioInserto, fechaInserto, usuarioModifico, fechaModifico, Eliminado, Activo) 
VALUES 
('SELECT * FROM tabla1', 'admin', GETDATE(), 'admin', GETDATE(), 0, 1),
('SELECT * FROM tabla2', 'admin', GETDATE(), 'admin', GETDATE(), 0, 1),
('print(''Hola Mundo'') - Python', 'admin', GETDATE(), 'admin', GETDATE(), 0, 1),
('console.log(''Hola Mundo'') - React', 'admin', GETDATE(), 'admin', GETDATE(), 0, 1);

-- Insertar Torneos
INSERT INTO TTorneo (anio, usuarioInserto, fechaInserto, usuarioModifico, fechaModifico, Eliminado, Activo) 
VALUES 
(2023, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1),
(2024, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1);

-- Insertar Luchadores
INSERT INTO TUser (username, email, password, imagen, usuarioInserto, fechaInserto, usuarioModifico, fechaModifico, Eliminado, Activo) 
VALUES 
('Hulk Hogan', 'hogan@.goku.com', 'hogan', 'https://www.google.com', 'admin', GETDATE(), 'admin', GETDATE(), 0, 1),
('The Rock', 'rock@.goku.com', 'rock', 'https://www.google.com', 'admin', GETDATE(), 'admin', GETDATE(), 0, 1),
('John Cena', 'cena@.goku.com', 'cena', 'https://www.google.com', 'admin', GETDATE(), 'admin', GETDATE(), 0, 1);

-- Insertar Inscripciones de Luchadores en Torneos
INSERT INTO TInscripcion (luchadorId, torneoId, ki, esferas, usuarioInserto, fechaInserto, usuarioModifico, fechaModifico, Eliminado, Activo) 
VALUES 
(1, 1, 66.66, 3, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- Hulk Hogan en 2023
(1, 2, 70.00, 4, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- Hulk Hogan en 2024
(2, 1, 66.66, 3, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- The Rock en 2023
(2, 2, 68.00, 3, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- The Rock en 2024
(3, 1, 66.66, 3, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- John Cena en 2023
(3, 2, 67.00, 3, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1); -- John Cena en 2024
INSERT INTO TInscripcion (luchadorId, torneoId, ki, esferas, usuarioInserto, fechaInserto, usuarioModifico, fechaModifico, Eliminado, Activo) 
VALUES 
(4, 2, 80.00, 3, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- John Cena en 2024
(5, 2, 85.00, 3, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1); -- John Cena en 2024

-- Relacionar Torneos con Categorías
INSERT INTO TTorneoCategoria (torneoId, categoriaId, usuarioInserto, fechaInserto, usuarioModifico, fechaModifico, Eliminado, Activo) 
VALUES 
(1, 1, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- Base de Datos en 2023
(1, 2, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- Backend en 2023
(1, 3, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- Frontend en 2023
(2, 1, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- Base de Datos en 2024
(2, 2, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- Backend en 2024
(2, 3, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1); -- Frontend en 2024

-- Relacionar Categorías con Requerimientos
INSERT INTO TCategoriaRequerimiento (categoriaId, requerimientoId, usuarioInserto, fechaInserto, usuarioModifico, fechaModifico, Eliminado, Activo) 
VALUES 
(1, 1, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- SELECT * FROM tabla1 en Base de Datos
(1, 2, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- SELECT * FROM tabla2 en Base de Datos
(2, 3, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- print(''Hola Mundo'') en Backend
(3, 4, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1); -- console.log(''Hola Mundo'') en Frontend

-- Insertar Notas de Requerimientos por Luchador y Torneo
INSERT INTO TNotaRequerimiento (requerimientoId, luchadorId, torneoId, nota, usuarioInserto, fechaInserto, usuarioModifico, fechaModifico, Eliminado, Activo) 
VALUES 
(1, 1, 1, 30.00, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- Hulk Hogan en 2023, Base de Datos, SELECT * FROM tabla1
(2, 1, 1, 20.00, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- Hulk Hogan en 2023, Base de Datos, SELECT * FROM tabla2
(3, 1, 1, 30.00, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- Hulk Hogan en 2023, Backend, print(''Hola Mundo'')
(4, 1, 1, 40.00, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- Hulk Hogan en 2023, Frontend, console.log(''Hola Mundo'')
(1, 2, 1, 30.00, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- The Rock en 2023, Base de Datos, SELECT * FROM tabla1
(2, 2, 1, 20.00, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- The Rock en 2023, Base de Datos, SELECT * FROM tabla2
(3, 2, 1, 30.00, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- The Rock en 2023, Backend, print(''Hola Mundo'')
(4, 2, 1, 40.00, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1); -- The Rock en 2023, Frontend, console.log(''Hola Mundo'')
INSERT INTO TNotaRequerimiento (requerimientoId, luchadorId, torneoId, nota, usuarioInserto, fechaInserto, usuarioModifico, fechaModifico, Eliminado, Activo) 
VALUES 
(1, 4, 2, 50.00, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- Hulk Hogan en 2023, Base de Datos, SELECT * FROM tabla1
(2, 4, 2, 30.00, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- Hulk Hogan en 2023, Base de Datos, SELECT * FROM tabla2
(3, 4, 2, 30.00, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- Hulk Hogan en 2023, Backend, print(''Hola Mundo'')
(4, 4, 2, 40.00, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- Hulk Hogan en 2023, Frontend, console.log(''Hola Mundo'')
(1, 5, 2, 30.00, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- Hulk Hogan en 2023, Base de Datos, SELECT * FROM tabla1
(2, 5, 2, 50.00, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- Hulk Hogan en 2023, Base de Datos, SELECT * FROM tabla2
(3, 5, 2, 30.00, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1), -- Hulk Hogan en 2023, Backend, print(''Hola Mundo'')
(4, 5, 2, 40.00, 'admin', GETDATE(), 'admin', GETDATE(), 0, 1) -- Hulk Hogan en 2023, Frontend, console.log(''Hola Mundo'')


SELECT t_inscripcion.id AS t_inscripcion_id, t_inscripcion.[luchadorId] AS [t_inscripcion_luchadorId], t_inscripcion.[torneoId] AS [t_inscripcion_torneoId], t_inscripcion.ki AS t_inscripcion_ki, t_inscripcion.esferas AS t_inscripcion_esferas, t_inscripcion.[Eliminado] AS [t_inscripcion_Eliminado], t_inscripcion.[Activo] AS [t_inscripcion_Activo] \nFROM t_inscripcion JOIN [TTorneo] ON [TTorneo].id = t_inscripcion.[torneoId] JOIN [TUser] ON [TUser].id = t_inscripcion.[luchadorId] \nWHERE [TTorneo].id = ?]\n[parameters:


SELECT t_inscripcion.id AS t_inscripcion_id, t_inscripcion.[luchadorId] AS [t_inscripcion_luchadorId], t_inscripcion.[torneoId] AS [t_inscripcion_torneoId], t_inscripcion.ki AS t_inscripcion_ki, t_inscripcion.esferas AS t_inscripcion_esferas, t_inscripcion.[Eliminado] AS [t_inscripcion_Eliminado], t_inscripcion.[Activo] AS [t_inscripcion_Activo] 
FROM t_inscripcion JOIN [TTorneo] ON [TTorneo].id = t_inscripcion.[torneoId]