from modelo_carro import vehiculo
class carro_publico(vehiculo):
    def __init__(self, modelo, motor, tipo_combustible, numero_pasajeros, ruta, color):
        super().__init__(modelo, motor, color, tipo_combustible)
        self.numero_pasajeros = numero_pasajeros
        self.ruta = ruta

    def imprimir_info(self):
        super().imprimir_info()
        print(f"El número de pasajeros es: {self.numero_pasajeros}")
        print(f"La ruta es: {self.ruta}")
        return "Información del carro público impresa correctamente."
    
    def iniciar_ruta(self):
        return f"El carro inicia la ruta {self.ruta}."

    def recoger_pasajeros(self, cantidad):
        return f"Se recogieron {cantidad} pasajeros."