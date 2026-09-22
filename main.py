# Req.1: Registrar solicitud
def registrar_solicitud(codigo, nombre, tipo, descripcion):
    if not validar_codigo(codigo) or nombre == "" or tipo == "" or descripcion == "":
        return "Error: datos inválidos"
    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "descripcion": descripcion
    }
    return solicitud

# Req.2: Validar código
def validar_codigo(codigo):
    return len(codigo) >= 5 and codigo.strip() != ""

def mostrar_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Registrar solicitud")
    print("2. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        tipo = input("Tipo: ")
        descripcion = input("Descripción: ")
        sol = registrar_solicitud(codigo, nombre, tipo, descripcion)
        print(sol)

    elif opcion == "2":
        print("Saliendo del sistema... ¡Hasta pronto!")
        break
    else:
        print("Opción inválida, intenta de nuevo.")
