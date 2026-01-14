import sqlite3

DB = "prision.db"

def login():
    usuario = input("Usuario: ")
    password = input("Password: ")

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # ✅ CONSULTA SEGURA (parametrizada)
    query = """
    SELECT * FROM usuarios
    WHERE username = ? AND password = ?
    """
    print("[DEBUG] Consulta preparada (segura)")
    print(query)

    cursor.execute(query, (usuario, password))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        print("[+] Login exitoso")
    else:
        print("[-] Login fallido")

def buscar_preso():
    termino = input("ID o nombre del preso: ")

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # ✅ CONSULTA SEGURA
    query = """
    SELECT id_preso, nombre, apellidos
    FROM presos
    WHERE id_preso = ? OR nombre LIKE ?
    """
    print("[DEBUG] Consulta preparada (segura)")
    print(query)

    cursor.execute(query, (termino, f"%{termino}%"))
    resultados = cursor.fetchall()
    conn.close()

    for r in resultados:
        print(r)

def insertar_visita():
    id_preso = input("ID preso: ")
    visitante = input("Nombre visitante: ")
    fecha = input("Fecha visita (YYYY-MM-DD): ")

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # ✅ INSERT SEGURO
    query = """
    INSERT INTO visitas (id_preso, nombre_visitante, fecha_visita)
    VALUES (?, ?, ?)
    """
    print("[DEBUG] Inserción segura")
    print(query)

    cursor.execute(query, (id_preso, visitante, fecha))
    conn.commit()
    conn.close()

    print("[+] Visita insertada")

def menu():
    while True:
        print("\n1. Login")
        print("2. Buscar preso")
        print("3. Insertar visita")
        print("4. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            login()
        elif opcion == "2":
            buscar_preso()
        elif opcion == "3":
            insertar_visita()
        elif opcion == "4":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()
