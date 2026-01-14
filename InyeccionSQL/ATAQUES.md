
# Informe de Ataques – SQL Injection (Red Team)

Este documento recoge los ataques de Inyección SQL realizados por el equipo Red Team sobre la aplicación vulnerable del proyecto “Inyección SQL – Blue Team”.  
Los ataques se llevaron a cabo en un entorno controlado, asumiendo un escenario de acceso interno al sistema objetivo mediante conexión SSH, con el fin de evaluar el impacto real de las vulnerabilidades presentes en la aplicación.


## Alcance del ataque

- Sistema objetivo: Aplicación de consola en Python conectada a SQLite
- Equipo atacante: Red Team (Kali Linux)
- Equipo objetivo: Blue Team (Desktop Linux)
- Tipo de acceso: Acceso interno mediante SSH (escenario de compromiso previo)
- Entorno: Laboratorio controlado en VirtualBox

La aplicación no expone servicios de red, por lo que los ataques se realizaron desde un contexto interno, simulando un escenario realista de post-explotación.


## Vulnerabilidades identificadas

Durante el análisis del código se identificaron múltiples vulnerabilidades de Inyección SQL debidas al uso de concatenación directa de entradas del usuario en las consultas SQL, sin validación ni uso de consultas parametrizadas.


### Bypass de autenticación

**Función afectada:** login()  
**Tipo de vulnerabilidad:** SQL Injection (Authentication Bypass)

La función de login construye la consulta SQL concatenando directamente el usuario y la contraseña proporcionados por el usuario.

' OR '1'='1

El sistema permitió el acceso sin credenciales válidas, omitiendo completamente el mecanismo de autenticación.

- Acceso no autorizado al sistema
- Compromiso total del mecanismo de autenticación

Ver capturas


### Extracción de datos mediante SQL Injection

**Función afectada:** buscar_preso()  
**Tipo de vulnerabilidad:** SQL Injection (Data Exposure)

El campo de búsqueda permite la inyección directa de código SQL, lo que posibilita alterar la cláusula WHERE.

' OR '1'='1

Se obtuvo el listado completo de presos almacenados en la base de datos, independientemente del criterio de búsqueda.

- Exposición de información sensible
- Pérdida de confidencialidad de los datos

Ver capturas


### Manipulación de datos mediante SQL Injection

**Función afectada:** insertar_visita()  
**Tipo de vulnerabilidad:** SQL Injection (Data Manipulation)

La función de inserción construye la consulta INSERT concatenando directamente los valores introducidos por el usuario.

hacker'); --

Se logró alterar el comportamiento de la consulta SQL, insertando datos manipulados sin ningún tipo de validación.

- Alteración de la integridad de la base de datos
- Posible corrupción de datos

Ver capturas


## Conclusiones

La aplicación vulnerable presenta fallos críticos de seguridad que permiten bypass de autenticación, extracción de información y manipulación de datos mediante Inyección SQL.  
La versión segura demuestra que la correcta implementación de consultas parametrizadas elimina completamente estos vectores de ataque.

Este ejercicio demuestra la importancia de aplicar buenas prácticas de desarrollo seguro y valida la efectividad de las medidas defensivas implementadas por el Blue Team.


## Estructura final esperada

├── ATAQUES.md
└── capturas/
    ├── exploit_login_bypass.png
    ├── exploit_data_extraction.png
    ├── exploit_insert_manipulation.png




