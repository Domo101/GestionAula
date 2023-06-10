import csv
import json
import random


def guardar_clase(clase):
    """guarda la clase en un fichero"""
    # escribir en un archivo

    # w: para escribir en el
    # r: para leer
    # +: para crearlo si no existe
    archivo = open("./bd.json", "w+")

    # pasamos la clase a un string en formato json
    clase_en_json = json.dumps(clase)

    # lo enchuflamos al archivo
    archivo.write(clase_en_json)

    # cerramos archivo
    archivo.close()


def cargar_clase():
    """cargar la clase desde un fichero"""
    try:
        archivo = open("bd.json", "r")

        # leemos el archivo
        clase_en_json = archivo.read()

        # pasar el string a un array
        clase = json.loads(clase_en_json)

        # cerramos el archivo
        archivo.close()

    except FileNotFoundError:
        print("No se ha encontrado bd.json")
        clase = list()

    # retornamos el array de la clase
    return clase


def nuevo_alumno():
    """pedir nuevo alumno al ususario"""
    alumno = dict(nombre=input("inserte nuevo alumno: "),
                  positivos=0,
                  faltas=0)
    print(f"Saludos {alumno['nombre']}!")
    return alumno

def borrar_alumno():
    """pedir que el usuario borre un alumno de la lista"""
    mostrar_clase(clase)
    i = input("numero de alumno a borrar de la lista: ")
    print("Bye bye " + str(clase[int(i)-1]['nombre']) + "!")
    del clase[int(i)-1]
    #print("bye bye alumno numero " + str(int(i)) + "!")
    mostrar_clase(clase)


def esta_en_clase(alumno_entrada, clase):
    """comprobar si alumno esta en la clase"""
    for alumno in clase:
        if alumno["nombre"] == alumno_entrada["nombre"]:
            return True
    return False


def seleccionar_alumno_random(clase):
    indice_random = random.randint(0, len(clase) - 1)
    return clase[indice_random]


def print_alumno(alumno):
    return f"{alumno['nombre'].capitalize()} ({alumno['positivos']})"


def mostrar_clase(clase):
    """mostrar la clase por pantalla"""
    num_alumno = 0
    for alumno in clase:
        num_alumno = num_alumno + 1
        # num_alumno: nombre_alumno
        print(f"{num_alumno}: {print_alumno(alumno)}")


def volcar_datos(clase):
    with open('clase.csv', 'w', newline='') as archivo_csv:
        nombres_columnas = ['nombre', 'positivos']
        writer = csv.DictWriter(archivo_csv, fieldnames=nombres_columnas)

        writer.writeheader()
        for alumno in clase:
            writer.writerow(alumno)


def seleccionar_alumno(clase):
    mostrar_clase(clase)
    num_alumno = int(input("Alumno: "))
    return clase[num_alumno - 1]


def positivo(alumno, clase):
    for al in clase:
        if alumno["nombre"] == al["nombre"]:
            al["positivos"] = al["positivos"] + 1
            print(f"Positivo: {print_alumno(al)}")


def faltas(alumno, clase):
    for al in clase:
        if alumno["nombre"] == al["nombre"]:
            al["faltas"] = al["faltas"] + 1
            print(f"faltas: {print_alumno(al)}")


def negativo(alumno, clase):
    for al in clase:
        if alumno["nombre"] == al["nombre"]:
            al["positivos"] = al["positivos"] - 1
            print(f"Positivo: {print_alumno(al)}")


def submenu_seleccionar(clase):
    """submenu de acciones sobre alumno"""
    alumno = seleccionar_alumno(clase)
    print(f"Seleccionado: {print_alumno(alumno)}")
    decision = ""
    while decision != "r":
        decision = input(
            "Seleccionar \n\t(+/positivo) \n\t(-/negativo) \n\t(f/faltas) \n\t(r/return)\n-> ")
        if decision == "+":
            positivo(alumno, clase)
        elif decision == "-":
            negativo(alumno, clase)
        elif decision == "f":
            faltas(alumno, clase)

        guardar_clase(clase)


def bucle_decisiones(clase):
    """bucle de decisiones"""
    decision = ""
    while decision != "q":
        decision = input(
            "Accion \n\t(q/salir) \n\t(r/random) \n\t(m/mostrar) \n\t(v/volcar) \n\t(s/seleccionar) \n\t(b/borrar) \n\t(n/nuevo)\n-> ")
        if decision == "m":
            # mostrar clase
            mostrar_clase(clase)
        elif decision == "r":
            # seleccionar alumno random
            print(
                f"Seleccionado: {print_alumno(seleccionar_alumno_random(clase))}")
        elif decision == "n":
            # nuevo alumno
            n_alumno = nuevo_alumno()

            # comprobar si esta en clase
            if not esta_en_clase(n_alumno, clase):
                # si no esta meterlo en la clase y ordenar
                clase.append(n_alumno)
                # guardamos la clase
                guardar_clase(clase)
            else:
                print(f"{n_alumno} ya esta en clase")
        elif decision == "v":
            volcar_datos(clase)
        elif decision == "s":
            submenu_seleccionar(clase)
        elif decision == "b":
            borrar_alumno()

# definir
clase = cargar_clase()

# bucle decisiones
try:
    bucle_decisiones(clase)
except KeyboardInterrupt:
    print("\nAdiosito!")
