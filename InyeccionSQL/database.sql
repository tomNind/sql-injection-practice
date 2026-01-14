PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS visitas;
DROP TABLE IF EXISTS condenas;
DROP TABLE IF EXISTS delitos;
DROP TABLE IF EXISTS presos;
DROP TABLE IF EXISTS celdas;
DROP TABLE IF EXISTS guardias;
DROP TABLE IF EXISTS usuarios;

-- =========================
-- USUARIOS (LOGIN)
-- =========================
CREATE TABLE usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    rol TEXT CHECK (rol IN ('admin', 'guardia')) NOT NULL
);

-- =========================
-- GUARDIAS
-- =========================
CREATE TABLE guardias (
    id_guardia INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    rango TEXT NOT NULL,
    id_usuario INTEGER,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- =========================
-- CELDAS
-- =========================
CREATE TABLE celdas (
    id_celda INTEGER PRIMARY KEY AUTOINCREMENT,
    modulo TEXT NOT NULL,
    capacidad INTEGER NOT NULL
);

-- =========================
-- PRESOS
-- =========================
CREATE TABLE presos (
    id_preso INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    fecha_ingreso DATE NOT NULL,
    id_celda INTEGER,
    FOREIGN KEY (id_celda) REFERENCES celdas(id_celda)
);

-- =========================
-- DELITOS
-- =========================
CREATE TABLE delitos (
    id_delito INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL,
    gravedad TEXT CHECK (gravedad IN ('leve', 'grave', 'muy grave')) NOT NULL
);

-- =========================
-- CONDENAS
-- =========================
CREATE TABLE condenas (
    id_condena INTEGER PRIMARY KEY AUTOINCREMENT,
    id_preso INTEGER NOT NULL,
    id_delito INTEGER NOT NULL,
    años_condena INTEGER NOT NULL,
    FOREIGN KEY (id_preso) REFERENCES presos(id_preso),
    FOREIGN KEY (id_delito) REFERENCES delitos(id_delito)
);

-- =========================
-- VISITAS
-- =========================
CREATE TABLE visitas (
    id_visita INTEGER PRIMARY KEY AUTOINCREMENT,
    id_preso INTEGER NOT NULL,
    nombre_visitante TEXT NOT NULL,
    fecha_visita DATE NOT NULL,
    FOREIGN KEY (id_preso) REFERENCES presos(id_preso)
);
