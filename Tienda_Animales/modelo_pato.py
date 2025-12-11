from modelo_animal import animal

class pato(animal):
    def __init__(self, nombre, habitat, edad, color, tipo_pico, envergadura):
        super().__init__(nombre, habitat, edad, color)
        self.tipo_pico = tipo_pico
        self.envergadura = envergadura  # en metros

    def imprimir_info(self):
        super().imprimir_info()
        print(f"Tipo de pico: {self.tipo_pico}")
        print(f"Envergadura: {self.envergadura} metros")
        return "informacion encontrada de pato"

    def graznar(self):
        return f"{self.nombre} está graznando."

    def nadar(self):
        return f"{self.nombre} está nadando"