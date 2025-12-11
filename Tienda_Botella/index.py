from modelo_botella import botella
from modelo_botella_plastico import botella_plastica
from modelo_botella_vidrio import botella_vidrio
from base_datos_botella import base_datos_botella

obj_base_datos = base_datos_botella()

print("=== Botella Normal ===")
marca = input("Marca: ")
capacidad = input("Capacidad: ")
tapa = input("Tipo de tapa: ")
obj1 = botella(marca, capacidad, tapa)
obj_base_datos.guardar_objeto(obj1)
obj_base_datos.imprimir_info()

print("\n=== Botella Plástica ===")
marca = input("Marca: ")
capacidad = input("Capacidad: ")
tapa = input("Tipo de tapa: ")
diseño = input("Diseño: ")
material = input("Material: ")
tinte = input("Tinte: ")
obj2 = botella_plastica(marca, capacidad, tapa, diseño, material, tinte)
obj_base_datos.guardar_objeto(obj2)
obj_base_datos.imprimir_info()

print("\n=== Botella de Vidrio ===")
marca = input("Marca: ")
capacidad = input("Capacidad: ")
tapa = input("Tipo de tapa: ")
forma = input("Forma: ")
grosor = input("Grosor: ")
transpariencia = input("Transpariencia: ")

obj3 = botella_vidrio(marca, capacidad, tapa, forma, grosor, transpariencia)
obj_base_datos.guardar_objeto(obj3)
obj_base_datos.imprimir_info()
