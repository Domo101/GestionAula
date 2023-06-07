def mostrar_clase(clase):
    num_alumno = 0
    for alumno in clase:
        num_alumno = num_alumno + 1
        # num_alumno: nombre_alumno
        print(f"{num_alumno}: {alumno.capitalize()}")

# definir
clase = ["acenha", "jorge", "alex"]

# ordenar
clase.sort()

# mostrar
mostrar_clase(clase)