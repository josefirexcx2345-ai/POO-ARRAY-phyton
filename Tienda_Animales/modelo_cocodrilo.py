from modelo_animal import animal

class cocodrilo(animal):
    def __init__(self, nombre, habitat, edad, color, longitud, peso):
        super().__init__(nombre, habitat, edad, color)
        self.longitud = longitud  # en metros
        self.peso = peso  # en kilogramos

    def imprimir_info(self):
        super().imprimir_info()
        print(f"Longitud: {self.longitud} cm")
        print(f"Peso: {self.peso} kg")
        return "informacion encontrada de cocodrilo"

    def nadar(self, velocidad):
        return f"{self.nombre} está nadando a {velocidad} km/h."

    def cazar(self, presa):
        return f"{self.nombre} está cazando a {presa}."