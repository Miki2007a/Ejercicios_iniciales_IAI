#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo

import math

a = float(input("Introduce el valor de a (x cuadrado): "))
b = float(input("Introduce el valor de b (x): "))
c = float(input("Introduce el valor de c (término independiente): "))



if a == 0:
    print("Error: El valor de 'a' no puede ser cero en una ecuación de segundo grado.") 
else:
    print("Es una ecuación de segundo grado. Ahora la resolveremos.")

if ((b * b) - 4*a*c) < 0:
    print("Error: La raíz cuadrada es negativa, no se puede calcular.")
else:
    resultado_1 = (-b + math.sqrt((b * b) - 4 * a * c)) / (2 * a)
    resultado_2 = (-b - math.sqrt((b * b) - 4 * a * c)) / (2 * a)
    print(f"Las soluciones son: {resultado_1:.2f} y {resultado_2:.2f}")
