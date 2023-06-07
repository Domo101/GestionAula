def mostrar_clase(clase):
    """mostrar la clase por pantalla"""
    num_alumno = 0
    for alumno in clase:
        num_alumno = num_alumno + 1
        # num_alumno: nombre_alumno
        # print(str(num_alumno) + ": " + alumno)
        print(f"{num_alumno}: {alumno.capitalize()}")

def nuevo_alumno():
    """pedir nuevo alumno al ususario"""
    alumno = input("inserte nuevo alumno: ")
    print(f"Saludos {alumno}!")
    return alumno

# definir
clase = ["acenha", "jorge", "alex"]

# nuevo alumno
n_a = nuevo_alumno()

# añadir
clase.append(n_a)

# ordenar
clase.sort()

# mostrar
mostrar_clase(clase)