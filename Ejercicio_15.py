#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.

import math

radio= int(input("Introduce el radio de tu cilindro: "))
altura= int(input("Introduce la altura de tu cilindro: "))

area= round(2 * math.pi * radio * (altura + radio), 2)
volumen= round((radio ** 2) * math.pi * altura, 2)

print("El área de tu cilindro es: ", area)
print("El volumen de tu cilindro es: ", volumen)