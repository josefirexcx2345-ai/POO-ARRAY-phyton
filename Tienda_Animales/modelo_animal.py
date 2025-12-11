class animal:
    def __init__(self, nombre, habitat, edad, color):
        self.nombre = nombre
        self.habitat = habitat
        self.edad = edad
        self.color = color

    def imprimir_info(self):
        print(f"Nombre del animal: {self.nombre}")
        print(f"Hábitat: {self.habitat}")
        print(f"Edad: {self.edad} años")
        print(f"Color: {self.color}")