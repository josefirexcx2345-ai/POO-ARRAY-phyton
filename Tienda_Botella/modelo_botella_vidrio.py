from modelo_botella import botella

class botella_vidrio(botella):
    def __init__(self, marca, capacidad, tapa, forma, grosor, transpariencia):
        super().__init__(marca, capacidad, tapa)
        self.forma = forma
        self.grosor = grosor
        self.transpariencia = transpariencia

    def reutilizar_botella(self):
        print(f"La botella se va a reutilizar: {self.forma}")

    def imprimir_info(self):
        print()   # ← línea en blanco
        print(f"la forma es: {self.forma} ")
        print(f"el grosor es: {self.grosor} ")
        print(f"la transpariencia es: {self.transpariencia} ")
        super().imprimir_info()
        print(f"la info de la tapa padre es: {self.tapa}")
        return "informacion encontrada de botella vidrio" 
