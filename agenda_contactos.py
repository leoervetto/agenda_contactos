
def mostrar_menu():
    print("\n1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir del Agenda de Contactos")
    print("\n")

def agregar_contacto(agenda):
    nombre = input("por favor ingrese el nombre completo del contacto: ")
    telefono = input("por favor ingrese el telefono del contacto: ")
    email = input("por favor ingrese el email del contacto: ")
    agenda[nombre] = {"telefono": telefono, "email": email}
    print(f"¡se ha agregado el contacto {nombre} exitosamente!")

def eliminar_contacto(agenda):
    nombre = input("por favor ingrese el nombre del contacto que desea eliminar: ")
    if nombre in agenda:
        seguro = input(f"Está seguro que desea eliminar a {nombre} de su lista de contactos (s / n): ")
        if seguro == "s":
            del agenda[nombre]
            print(f"el contacto de {nombre} se ha eliminado exitosamente")
        elif seguro == "n":
            print(f"el contacto de {nombre} no ha sido eliminado")
        else:
            print("ingrese una opción válida (s / n)")
    else:
        print(f"el nombre {nombre} no se encuentra en la lista de contactos")

def buscar_contacto(agenda):
    nombre = input("ingrese el nombre del contacto que busca: ")
    if nombre in agenda:
        print(f"\nNombre: {nombre}")
        print(f"telefono: {agenda[nombre]["telefono"]}")
        print(f"email: {agenda[nombre]["email"]}")

    else:
        print(f"el contacto {nombre} no se encuentra en su agenda de contactos")
        

def lista_contactos(agenda):
    if agenda:
        print("Lista de contactos: \n ")
        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"telefono: {info["telefono"]}")
            print(f"email: {info["email"]}")
            print("-" * 20)
    else:
        print("no tiene ningun contacto en la agenda.")



def agenda_contactos():
    agenda = {}
    
    while True:
        mostrar_menu()
        opcion = input("Por favor elija una opción: ")
        print("\n")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            lista_contactos(agenda)
        elif opcion == "5":
            print("Saliendo del programa")
            break
        else:
            print("Por favor elija una opción válida (un número del 1 a 5)")

agenda_contactos()