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

    while True:

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

def BuscarContactoPorTelefono():

    while True:

        limpiarPantalla()

        telefonoABuscar = input("Ingrese el teléfono a buscar: ")

        if not os.path.exists("AgendaDeContacto.txt"):
            print("\n Aún no hay contactos cargados...")
            input("Presione ENTER para continuar") 
            return

        encontrado = False

        with open("AgendaDeContacto.txt","r",encoding="utf-8") as archivo:
            for linea in archivo:
              partes = linea.strip().split("|")

              if partes[2] == telefonoABuscar:
                limpiarPantalla()

                print("===== CONTACTO ENCONTRADO ====\n")
                print(f"Nombre: {partes[0]}")
                print(f"Apellido: {partes[1]}")
                print(f"Teléfono: {partes[2]}")
                print(f"Email: {partes[3]}")
                print("============================\n")
                encontrado=True
                break
        
        if not encontrado:
            print("El teléfono ingresado no se encontró en ningún contacto. \n")


        respuesta = input("¿Desea buscar otro contacto por el teléfono? (s/n): ").lower()

        while respuesta != 's' or respuesta != 'n':
            print("ERROR: Debes ingresar 's' o 'n' \n")
            respuesta = input("¿Desea buscar otro contacto por el teléfono? (s/n): ").lower()

        if respuesta == 'n':
            return    

def EliminarContacto():

    limpiarPantalla()

    telefonoEliminar = input("Ingrese el teléfono del contacto a eliminar: ")
    contactosActualizados = []
    eliminado = False

    with open("AgendaDeContacto.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            nombre, apellido, telefono, email = linea.strip().split("|")

            if telefono != telefonoEliminar:
                contactosActualizados.append(linea)
            else:
                eliminado = True

    if eliminado:
        with open("AgendaDeContacto.txt", "w", encoding="utf-8") as archivo:
            archivo.writelines(contactosActualizados)

        print("Contacto eliminado correctamente.")
    else:
        print("No se encontró el contacto.")

    input("ENTER para continuar...")


def Salir():

    print("SALIENDO DEL PROGRAMA...")


def MenuPrincipal():

    while True:

        limpiarPantalla()

        print("-------------------")    

        print("Agenda de contacto")      

        print("------------------\n") 

        print("1 > Alta de Contacto")

        print("2 > Buscar Contacto por teléfono")

        print("3 > Eliminar contacto")

        print("0 > Salir \n") 


        opcion = input("|> Escriba la opción seleccionada: ")

        while not opcion.isdigit():
            print("\n ERROR: DEBES SER UN NÚMERO VÁLIDO")
            opcion = input("|> Escriba la opción seleccionada: ")

        opcion = int(opcion)

        if opcion == 1:
            AltaDeContacto()
        elif opcion == 2:
            BuscarContactoPorTelefono()
        elif opcion == 3:
            EliminarContacto()
        elif opcion == 0:
            Salir()
        else:
            print("LA OPCIÓN INGRESADA ES INCORRECTA. INTENTE DE NUEVO...")


MenuPrincipal()                        
