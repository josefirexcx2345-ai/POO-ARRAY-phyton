class base_datos_vehiculo:

    def __init__(self):
        self.lista_vehiculos = []      
        self.lista_publicos = []       
        self.lista_deportivos = []    
        self.lista_carga = []          

    def guardar_objeto(self, nuevo_objeto):
        self.lista_vehiculos.append(nuevo_objeto)
        print(nuevo_objeto)   

    def agregar_varios_objeto(self, lista_nueva):
        self.lista_vehiculos.extend(lista_nueva)
        for obj in lista_nueva:
            print(obj)

    def imprimir_info(self):
        for vehiculo in self.lista_vehiculos:
            vehiculo.imprimir_info()
            print("-----------------------------")
