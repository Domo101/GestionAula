class Vehiculo:
    def __init__(self, matricula):
        self.matricula = matricula

    def arrancar(self):
        print(f"{self.matricula}, bbbbruuummm!")

    def girar(self):
        pass

class Coche(Vehiculo):
    def __init__(self, matricula):
        super().__init__(matricula)
        self.potencia = 100

    def cicrcular(self):
        print(f"me circulo {self.potencia}")

    def girar(self):
        print("girando")

class Avion(Vehiculo):
    def __init__(self, matricula):
        super().__init__(matricula)
        self.potencia = 100

    def volar(self):
        print("me vuelo")

    def girar(self):
        print("inclinando")

def girar_vehiculo(vehiculo):
    vehiculo.girar()


coche = Coche("123")
avion = Avion("1223")

girar_vehiculo(coche)
girar_vehiculo(avion)

coche.arrancar()