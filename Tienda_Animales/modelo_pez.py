from modelo_animal import animal

class pez(animal):
    def __init__(self, nombre, habitat, edad, color, tipo_agua, longitud):
        super().__init__(nombre, habitat, edad, color)
        self.tipo_agua = tipo_agua  # dulce o salada
        self.longitud = longitud  # en centímetros

    def imprimir_info(self):
        super().imprimir_info()
        print(f"Tipo de agua: {self.tipo_agua}")
        print(f"Longitud: {self.longitud} cm")
        return "informacion encontrada de pez"

    def nadar(self, velocidad):
        return f"{self.nombre} está nadando a {velocidad} cm/s."

    def saltar(self, altura):
        return f"{self.nombre} está saltando a una altura de {altura} cm."