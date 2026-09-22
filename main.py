# Req.2: Validar código
def validar_codigo(codigo):
    # El código no puede estar vacío y debe tener al menos 5 caracteres
    if codigo.strip() == "":
        return False
    if len(codigo) < 5:
        return False
    return True

# Req.3: Validar tipo
def validar_tipo(tipo):
    tipos_validos = ["matricula", "pagos", "plataforma", "otro"]
    return tipo.lower() in tipos_validos

# Req.1: Registrar solicitud
def registrar_solicitud(codigo, nombre, tipo, descripcion):
    # Validaciones combinadas
    if not validar_codigo(codigo):
        return "Error: código inválido"
    if nombre.strip() == "":
        return "Error: nombre inválido"
    if not validar_tipo(tipo):
        return "Error: tipo inválido"
    if descripcion.strip() == "":
        return "Error: descripción inválida"

    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "descripcion": descripcion
    }
    return solicitud

# Req.4: Mostrar menú principal
def mostrar_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Registrar solicitud")
    print("2. Salir")

# Programa principal interactivo
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        tipo = input("Tipo (matricula/pagos/plataforma/otro): ")
        descripcion = input("Descripción: ")

        resultado = registrar_solicitud(codigo, nombre, tipo, descripcion)
        print(resultado)

    elif opcion == "2":
        print("Saliendo del sistema... ¡Hasta pronto!")
        break
    else:
        print("Opción inválida, intenta de nuevo.")
