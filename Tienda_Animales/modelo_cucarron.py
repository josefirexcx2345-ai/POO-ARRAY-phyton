from modelo_animal import animal

class cucarron(animal):
    def __init__(self, nombre, habitat, edad, color, tipo_alas, numero_patitas):
        super().__init__(nombre, habitat, edad, color)
        self.tipo_alas = tipo_alas
        self.numero_patitas = numero_patitas

    def imprimir_info(self):
        super().imprimir_info()
        print(f"Tipo de alas: {self.tipo_alas}")
        print(f"Número de patitas: {self.numero_patitas}")
        return "informacion encontrada de cucarron"

    def volar(self, altura):
        return f"{self.nombre} está volando a una altura de {altura} metros."
