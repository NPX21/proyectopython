agenda_telefonica = dict()
print()
print("Bienvenido a su agenda telefónica personalizada ")
print()
def agregar_contacto():
    print()
    nombre = input("Nombre del contacto que quieres añadir: ")
    numero = input("Numero del contacto que quieres añadir: ")
    agenda_telefonica[nombre] = numero
    nombre_operacion = ("El contacto ha sido añadido con éxito")
    print()
    print(nombre_operacion)
    print()

def remover_contacto():
    print()
    nombre = input("Nombre del contacto que quieres eliminar: ")
    nombre_operacion = None

    try:
        del agenda_telefonica[nombre]
    except KeyError:
        print("Ese contacto no existe")
    else:
        print()
        print("El contacto ha sido borrado con éxito")
        print()

def actualizar_contacto():
    print()
    print("Actualizar Contacto")
    print()
    nombre = input("Nombre del contacto que quieres actualizar: ")
    numero = input("Nuevo numero del contacto: ")
    agenda_telefonica[nombre] = numero
    print()
    print("El numero ha sido actualizado con éxito")
    print()

def ver_todos_contacto():
    print()
    print("Lista de contactos")
    nombre_operacion = None

    if len(agenda_telefonica) == 0:
        nombre_operacion = ("No tienes guardado ningun contacto")
    else:
        for contacto in agenda_telefonica:
            if nombre_operacion == None:
                nombre_operacion = "{} - {}".format(contacto,agenda_telefonica[contacto])
            else:
                nombre_operacion += "\n{} - {}".format(contacto,agenda_telefonica[contacto])
    print()
    print(nombre_operacion)
    print()

while True:
    print("Estas son las operaciones que puedes realizar")
    print("1 - Añadir Contacto")
    print("2 - Eliminar Contacto")
    print("3 - Actualizar Contacto")
    print("4 - Ver todos mis contactos")
    print("5 - Salir")

    try:
        operacion = int(input("Has elegido la opción  "))
    except ValueError:

        print("Elige una opción del 1 al 5")

    else:
        if operacion == 1:
            agregar_contacto()
        elif operacion == 2:
            remover_contacto()
        elif operacion == 3:
            actualizar_contacto()
        elif operacion == 4:
            ver_todos_contacto()
        elif operacion == 5:
            break
        else:
            print()
            print("Esa operación no existe colega")
            print()
print()
print("Muchas gracias por utilizarme, vuelve pronto amigo")
