from modelo_animal import animal

class caballo(animal):
    def __init__(self, nombre, habitat, edad, color, raza, altura):
        super().__init__(nombre, habitat, edad, color)
        self.raza = raza
        self.altura = altura  # en metros

    def imprimir_info(self):
        super().imprimir_info()
        print(f"Raza: {self.raza}")
        print(f"Altura: {self.altura} metros")
        return "informacion encontrada de caballo"

    def relinchar(self):
        return f"{self.nombre} está relinchando."
