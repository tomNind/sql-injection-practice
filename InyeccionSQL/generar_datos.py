import sqlite3
from faker import Faker
import random

# Inicializar Faker
fake = Faker()

# Conexión a la base de datos SQLite
conn = sqlite3.connect("prision.db")
cursor = conn.cursor()

# Activar claves foráneas
cursor.execute("PRAGMA foreign_keys = ON;")

# =========================
# USUARIOS
# =========================
usuarios = []
for _ in range(5):
    username = fake.user_name()
    password = fake.password()
    rol = random.choice(["admin", "guardia"])
    usuarios.append((username, password, rol))

cursor.executemany(
    "INSERT INTO usuarios (username, password, rol) VALUES (?, ?, ?)",
    usuarios
)

# =========================
# GUARDIAS
# =========================
for i in range(1, 4):
    cursor.execute(
        "INSERT INTO guardias (nombre, rango, id_usuario) VALUES (?, ?, ?)",
        (
            fake.name(),
            random.choice(["Sargento", "Teniente", "Capitán"]),
            i
        )
    )

# =========================
# CELDAS
# =========================
for _ in range(4):
    cursor.execute(
        "INSERT INTO celdas (modulo, capacidad) VALUES (?, ?)",
        (
            random.choice(["A", "B", "C"]),
            random.randint(2, 6)
        )
    )

# =========================
# PRESOS
# =========================
for _ in range(10):
    cursor.execute(
        """
        INSERT INTO presos (nombre, apellidos, fecha_ingreso, id_celda)
        VALUES (?, ?, ?, ?)
        """,
        (
            fake.first_name(),
            fake.last_name(),
            fake.date_between(start_date="-5y", end_date="today"),
            random.randint(1, 4)
        )
    )

# =========================
# DELITOS
# =========================
delitos = [
    ("Robo", "leve"),
    ("Fraude", "grave"),
    ("Tráfico de drogas", "grave"),
    ("Homicidio", "muy grave")
]

cursor.executemany(
    "INSERT INTO delitos (descripcion, gravedad) VALUES (?, ?)",
    delitos
)

# =========================
# CONDENAS
# =========================
for _ in range(10):
    cursor.execute(
        """
        INSERT INTO condenas (id_preso, id_delito, años_condena)
        VALUES (?, ?, ?)
        """,
        (
            random.randint(1, 10),
            random.randint(1, 4),
            random.randint(1, 30)
        )
    )

# =========================
# VISITAS
# =========================
for _ in range(8):
    cursor.execute(
        """
        INSERT INTO visitas (id_preso, nombre_visitante, fecha_visita)
        VALUES (?, ?, ?)
        """,
        (
            random.randint(1, 10),
            fake.name(),
            fake.date_between(start_date="-1y", end_date="today")
        )
    )

# Guardar cambios y cerrar
conn.commit()
conn.close()

print("[+] Datos insertados correctamente en prision.db")
