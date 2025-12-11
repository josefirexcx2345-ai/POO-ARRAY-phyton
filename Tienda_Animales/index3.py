from modelo_animal import animal
from modelo_caballo import caballo
from modelo_cocodrilo import cocodrilo
from modelo_cucarron import cucarron
from modelo_pato import pato
from modelo_pez import pez
from base_datos2 import base_datos_animal

obj_base_datos = base_datos_animal()

print("=== ANIMAL (Normal) ===")
nombre = input("Nombre: ")
habitat = input("Hábitat: ")
edad = input("Edad: ")
color = input("Color: ")
obj1 = animal(nombre, habitat, edad, color)
obj_base_datos.guardar_objeto(obj1)

print("\n=== CABALLO ===")
nombre = input("Nombre: ")
habitat = input("Hábitat: ")
edad = input("Edad: ")
color = input("Color: ")
raza = input("Raza: ")
altura = input("Altura (m): ")
obj2 = caballo(nombre, habitat, edad, color, raza, altura)
obj_base_datos.guardar_objeto(obj2)

print("\n=== COCODRILO ===")
nombre = input("Nombre: ")
habitat = input("Hábitat: ")
edad = input("Edad: ")
color = input("Color: ")
longitud = input("Longitud (cm): ")
peso = input("Peso (kg): ")
obj3 = cocodrilo(nombre, habitat, edad, color, longitud, peso)
obj_base_datos.guardar_objeto(obj3)

print("\n=== CUCARRÓN ===")
nombre = input("Nombre: ")
habitat = input("Hábitat: ")
edad = input("Edad: ")
color = input("Color: ")
tipo_alas = input("Tipo de alas: ")
numero_patitas = input("Número de patitas: ")
obj4 = cucarron(nombre, habitat, edad, color, tipo_alas, numero_patitas)
obj_base_datos.guardar_objeto(obj4)

print("\n=== PATO ===")
nombre = input("Nombre: ")
habitat = input("Hábitat: ")
edad = input("Edad: ")
color = input("Color: ")
tipo_pico = input("Tipo de pico: ")
envergadura = input("Envergadura (m): ")
obj5 = pato(nombre, habitat, edad, color, tipo_pico, envergadura)
obj_base_datos.guardar_objeto(obj5)

print("\n=== PEZ ===")
nombre = input("Nombre: ")
habitat = input("Hábitat: ")
edad = input("Edad: ")
color = input("Color: ")
tipo_agua = input("Tipo de agua (dulce/salada): ")
longitud = input("Longitud (cm): ")
obj6 = pez(nombre, habitat, edad, color, tipo_agua, longitud)
obj_base_datos.guardar_objeto(obj6)
