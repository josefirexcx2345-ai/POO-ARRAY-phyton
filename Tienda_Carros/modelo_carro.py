class vehiculo:
    def __init__(self, modelo, motor, color, tipo_combustible,):
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.color = color

    def imprimir_info(self):
        print(f"Modelo del carro: {self.modelo}")
        print(f"Motor: {self.motor}")
        print(f"el tipo de combustible es: {self.tipo_combustible}")  
        print(f"el color del carro es: {self.color}")
