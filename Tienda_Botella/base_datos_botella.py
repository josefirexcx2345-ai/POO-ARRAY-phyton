class base_datos_botella:

    def __init__(self, ):
     self.lista_botellas = []
     self.lista_plastico = []
     self.lista_vidrio = []

    def guardar_objeto(self, nuevo_objeto):
        self.lista_botellas.append(nuevo_objeto)

    def agregar_varios_objeto(self):
        self.lista_botellas.extend(self.lista_nueva)

    def imprimir_info(self):
        for objeto in self.lista_botellas:
            print(objeto)