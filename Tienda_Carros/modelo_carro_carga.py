from modelo_carro import vehiculo
class carro_carga(vehiculo):
    def __init__(self, modelo, motor, tipo_combustible, color, capacidad_carga, numero_ejes):
        super().__init__(modelo, motor, tipo_combustible, color)
        self.capacidad_carga = capacidad_carga
        self.numero_ejes = numero_ejes

    def imprimir_info(self):
        super().imprimir_info()
        print(f"La capacidad de carga es: {self.capacidad_carga} kg")
        print(f"El número de ejes es: {self.numero_ejes}")
        return "Información del carro de carga impresa correctamente."
    
    def descripcion_carga(self):
        return f"Este vehículo puede cargar hasta {self.capacidad_carga} kg en {self.numero_ejes} ejes."