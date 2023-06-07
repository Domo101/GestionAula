import sys
import json
import random

def guardar_clase(clase):
    """guarda la clase en un fichero"""
    # escribir en un archivo

    # w: para escribir en el
    # r: para leer
    # +: para crearlo si no existe
    archivo = open("bd.json", "w+")

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
        clase = list()

    # retornamos el array de la clase
    return clase

def mostrar_clase(clase):
    """mostrar la clase por pantalla"""
    num_alumno = 0
    for alumno in clase:
        num_alumno = num_alumno + 1
        # num_alumno: nombre_alumno
        # print(str(num_alumno) + ": " + alumno)
        print(f"{num_alumno}: {alumno.capitalize()}")

def capturar_entrada_usuario():
    """pedir nuevo alumno al ususario"""
    alumno = input("inserte nuevo alumno: ")
    print(f"Saludos {alumno}!")
    return alumno

def capturar_argumento():
    """comprobar argumentos"""
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return "unknownsoldier"

def nuevo_alumno():
    """decidir de que manera se añade un nuevo alumno"""
    if len(sys.argv) > 1:
        return capturar_argumento()
    else:
        return capturar_entrada_usuario()

def esta_en_clase(alumno_entrada, clase):
    """comprobar si alumno esta en la clase"""
    for alumno in clase:
        if alumno == alumno_entrada:
            return True
    return False

def seleccionar_alumno_random(clase):
    indice_random = random.randint(0, len(clase) - 1)
    return clase[indice_random]

def bucle_decisiones(clase):
    """bucle de decisiones"""
    decision = ""
    while decision != "q":
        decision = input(
            "Accion \n\t(q/salir) \n\t(r/random) \n\t(m/mostrar) \n\t(n/nuevo)\n-> ")
        if decision == "m":
            # mostrar clase
            mostrar_clase(clase)
        elif decision == "r":
            # seleccionar alumno random
            print(
                f"Seleccionado: {seleccionar_alumno_random(clase)}")
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

# definir
clase = cargar_clase()

# bucle decisiones
bucle_decisiones(clase)