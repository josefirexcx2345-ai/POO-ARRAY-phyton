from modelo_carro import vehiculo

class carro_deportivo(vehiculo):
    def __init__(self, modelo, motor, color, tipo_combustible, velocidad_maxima, tipo_deportivo):
        super().__init__(modelo, motor, color, tipo_combustible)
        self.velocidad_maxima = velocidad_maxima 
        self.tipo_deportivo = tipo_deportivo    

    def imprimir_info(self):
        super().imprimir_info()
        print(f"La velocidad máxima es: {self.velocidad_maxima} km/h")
        print(f"El tipo de carro deportivo es: {self.tipo_deportivo}")
        return "Información del carro deportivo impresa correctamente."
    
    def encender(self):
        return f"El {self.tipo_deportivo} está encendido."

    def acelerar(self, velocidad):
        return f"El carro acelera a {velocidad} km/h."