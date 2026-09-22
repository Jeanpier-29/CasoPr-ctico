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
    # Verifica que el texto no esté vacío ni tenga solo espacios
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

# Req.4: Mostrar menú
def mostrar_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Registrar solicitud")
    print("2. Salir")

solicitudes = []

def agregar_solicitud(solicitud):
    if isinstance(solicitud, dict):
        solicitudes.append(solicitud)
        print("Solicitud registrada correctamente.")
        print(solicitud)
    else:
        print(solicitud)

# Main interactivo Req.1–6
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
        print("Saliendo del sistema... ¡Hasta pronto!")
        break
    else:
        print("Opción inválida, intenta de nuevo.")
