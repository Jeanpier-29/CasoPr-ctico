# Req.2: Validar código
def validar_codigo(codigo):
    if codigo.strip() == "":
        return False
    if len(codigo) < 5:
        return False
    return True

# Req.3: Validar tipo
def validar_tipo(tipo):
    tipos_validos = ["matricula", "pagos", "plataforma", "otro"]
    return tipo.lower() in tipos_validos

# Req.6: Validar texto
def validar_texto(texto):
    return texto.strip() != ""

# Req.5: Calcular prioridad
def calcular_prioridad(tipo):
    if tipo.lower() in ["matricula", "pagos", "plataforma"]:
        return "Alta"
    else:
        return "Baja"

# Req.1: Registrar solicitud
def registrar_solicitud(codigo, nombre, tipo, descripcion):
    if not validar_codigo(codigo):
        return "Error: código inválido"
    if nombre.strip() == "":
        return "Error: nombre inválido"
    if not validar_tipo(tipo):
        return "Error: tipo inválido"
    if not validar_texto(descripcion):
        return "Error: descripción inválida"

    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "descripcion": descripcion,
        "prioridad": calcular_prioridad(tipo)
    }
    return solicitud

# Req.7: Mostrar resumen
def mostrar_resumen(solicitud):
    if isinstance(solicitud, dict):
        print("=== Resumen de Solicitud ===")
        print(f"Código: {solicitud['codigo']}")
        print(f"Nombre: {solicitud['nombre']}")
        print(f"Tipo: {solicitud['tipo']}")
        print(f"Descripción: {solicitud['descripcion']}")
        print(f"Prioridad: {solicitud['prioridad']}")
    else:
        print(solicitud)

# Req.4: Mostrar menú
def mostrar_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Registrar solicitud")
    print("2. Consultar por código")
    print("3. Consultar por tipo")
    print("4. Salir")

# Req.8: Almacenar solicitudes
solicitudes = []

def agregar_solicitud(solicitud):
    if isinstance(solicitud, dict):
        solicitudes.append(solicitud)
        print("Solicitud registrada correctamente.")
        mostrar_resumen(solicitud)
    else:
        print(solicitud)

# Req.9: Consultar por código
def consultar_solicitud(codigo):
    for sol in solicitudes:
        if sol["codigo"] == codigo:
            mostrar_resumen(sol)
            return
    print(f"No se encontró ninguna solicitud con el código: {codigo}")

# Req.10: Consultar por tipo
def consultar_por_tipo(tipo):
    encontrados = [sol for sol in solicitudes if sol["tipo"].lower() == tipo.lower()]
    if encontrados:
        for sol in encontrados:
            mostrar_resumen(sol)
    else:
        print(f"No se encontraron solicitudes del tipo: {tipo}")

# Main interactivo Req.1–10
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        tipo = input("Tipo (matricula/pagos/plataforma/otro): ")
        descripcion = input("Descripción: ")
        sol = registrar_solicitud(codigo, nombre, tipo, descripcion)
        agregar_solicitud(sol)

    elif opcion == "2":
        codigo = input("Código a consultar: ")
        consultar_solicitud(codigo)

    elif opcion == "3":
        tipo = input("Tipo a consultar: ")
        consultar_por_tipo(tipo)

    elif opcion == "4":
        print("Saliendo del sistema... ¡Hasta pronto!")
        break
    else:
        print("Opción inválida, intenta de nuevo.")
