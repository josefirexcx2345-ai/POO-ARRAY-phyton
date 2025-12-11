class base_datos_animal:

    def __init__(self):
        self.lista_animales = []   

    def guardar_objeto(self, nuevo_objeto):
        self.lista_animales.append(nuevo_objeto)
        print(nuevo_objeto)

    def agregar_varios_objeto(self, lista_nueva):
        self.lista_animales.extend(lista_nueva)

    def imprimir_info(self):
        for animal in self.lista_animales:
            print(animal)
            print("-----------------------------")
