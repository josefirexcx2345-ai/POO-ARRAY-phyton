from modelo_botella import botella

class botella_plastica(botella):
    def __init__(self, marca, capacidad, tapa, diseño, material, tinte):
        super().__init__(marca, capacidad, tapa)
        self.diseño = diseño
        self.material = material
        self.tinte = tinte

    def reciclar_botella(self):
        print(f"La botella se va a reciclar: {self.material}") 

    def imprimir_info(self):
        print()   # ← línea en blanco
        print(f"el diseño es: {self.diseño} ")
        print(f"el material es: {self.material} ")
        print(f"el color es: {self.tinte} ")
        super().imprimir_info()
        print(f"la info de la tapa padre es: {self.tapa}")
        return "infromacion encontrada de botella plastica"
       