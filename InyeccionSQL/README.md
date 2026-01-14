
# Proyecto: Inyección SQL – Blue Team

## Descripción del proyecto
Este proyecto tiene como objetivo demostrar de forma práctica la vulnerabilidad de Inyección SQL y su correcta mitigación desde un enfoque Blue Team. Se ha desarrollado una aplicación de consola en Python conectada a una base de datos SQLite que simula un sistema real de gestión de una prisión. El proyecto permite analizar cómo una mala construcción de consultas SQL puede ser explotada por un atacante y cómo el uso de consultas parametrizadas previene este tipo de ataques.


## Estructura de archivos
El proyecto está organizado de la siguiente manera:

InyeccionSQL/
├── README.md
├── database.sql
├── prision.db
├── generar_datos.py
├── app_vulnerable.py
├── app_segura.py
├── requirements.txt


## Temática elegida
La temática del proyecto está basada en la gestión de una prisión. La base de datos representa un entorno realista que incluye usuarios del sistema (administradores y guardias), presos, celdas, delitos, condenas y visitas. Esta temática se eligió por su claridad para representar relaciones complejas y por ser adecuada para realizar pruebas de autenticación, búsquedas e inserciones, así como para demostrar ataques de Inyección SQL en un contexto real.


## Cómo ejecutar cada versión

### 1. Crear la base de datos
Desde la carpeta del proyecto, ejecutar:
sqlite3 prision.db < database.sql

### 2. Instalar dependencias
Ejecutar:
pip3 install -r requirements.txt

### 3. Generar datos de prueba
Ejecutar:
python3 generar_datos.py

### 4. Ejecutar la versión vulnerable
Ejecutar:
python3 app_vulnerable.py  
Esta versión permite demostrar ataques de Inyección SQL.

### 5. Ejecutar la versión segura
Ejecutar:
python3 app_segura.py  
Esta versión utiliza consultas parametrizadas y bloquea los ataques de Inyección SQL.


## Requisitos técnicos
Para ejecutar este proyecto se requiere:

- Sistema operativo Linux
- Python 3
- SQLite 3
- pip3
- Librería Faker para la generación de datos
- Entorno de pruebas controlado (VirtualBox)
