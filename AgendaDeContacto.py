import os

def limpiarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def emailValido(email):
    if "@" not in email or "." not in email:
        return False

    if email.startswith("@") or email.endswith("@"):
        return False

    if email.startswith(".") or email.endswith("."):
        return False

    if email.index("@") > email.rindex("."):
        return False

    return True


def AltaDeContacto():

    limpiarPantalla()

    print("Ingrese los datos para poder agregar el contacto... \n")

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    telefono = input("Ingrese su teléfono: ")

    while not telefono.isdigit() or int(telefono)<10:
        print("Error: Debe ser un número de teléfono mayor de 10 números...\n")
        telefono = input("Ingrese su teléfono: ")

    telefono = int(telefono)

    email = input("Ingrese su email: ")

    while not emailValido(email):
        print("Error: Email inválido. Ejemplo válido: usuario@email.com\n")
        email = input("Ingrese su email: ")

    email = int(email)    

    limpiarPantalla()

    print("========== NUEVO CONTACTO ==========")

    print(f"Nombre: {nombre}")

    print(f"Apellido: {apellido}")

    print(f"Teléfono: {telefono}")

    print(f"Email: {email}")

    print("==================================\n")

    with open("AgendaDeContacto.txt","a",encoding="utf-8") as archivo:
        archivo.write(f"{nombre}|{apellido}|{telefono}|{email}\n")

    respuesta = input("¿Desea agendar otro contacto? (s/n): ").lower()

    while respuesta != 's' or respuesta != 'n':
        input("Error: Debes ingresar 's' o 'n'. \n")    
        respuesta = input("¿Desea agendar otro contacto? (s/n): ").lower()

    if respuesta == 'n':
        return    