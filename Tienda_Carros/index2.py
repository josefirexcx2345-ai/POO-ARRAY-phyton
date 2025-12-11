from modelo_carro import vehiculo
from modelo_carro_publico import carro_publico
from modelo_carro_deportivo import carro_deportivo
from modelo_carro_carga import carro_carga
from base_datos import base_datos_vehiculo

obj_base_datos = base_datos_vehiculo()

print("=== Vehículo Normal ===")
modelo = input("Modelo: ")
motor = input("Motor: ")
color = input("Color: ")
tipo_combustible = input("Tipo de combustible: ")
obj1 = vehiculo(modelo, motor, color, tipo_combustible)
obj_base_datos.guardar_objeto(obj1)

print("\n=== Carro Público ===")
modelo = input("Modelo: ")
motor = input("Motor: ")
color = input("Color: ")
tipo_combustible = input("Tipo de combustible: ")
numero_pasajeros = input("Número de pasajeros: ")
ruta = input("Ruta: ")
obj2 = carro_publico(modelo, motor, tipo_combustible, numero_pasajeros, ruta, color)
obj_base_datos.guardar_objeto(obj2)

print("\n=== Carro Deportivo ===")
modelo = input("Modelo: ")
motor = input("Motor: ")
color = input("Color: ")
tipo_combustible = input("Tipo de combustible: ")
velocidad_maxima = input("Velocidad máxima: ")
tipo_deportivo = input("Tipo de deportivo (ej: Coupé, GT, etc): ")
obj3 = carro_deportivo(modelo, motor, color, tipo_combustible, velocidad_maxima, tipo_deportivo)
obj_base_datos.guardar_objeto(obj3)

print("\n=== Carro de Carga ===")
modelo = input("Modelo: ")
motor = input("Motor: ")
tipo_combustible = input("Tipo de combustible: ")
color = input("Color: ")
capacidad_carga = input("Capacidad de carga (kg): ")
numero_ejes = input("Número de ejes: ")
obj4 = carro_carga(modelo, motor, tipo_combustible, color, capacidad_carga, numero_ejes)
obj_base_datos.guardar_objeto(obj4)
