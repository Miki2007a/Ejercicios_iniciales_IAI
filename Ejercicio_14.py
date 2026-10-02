# 14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.

import math

diametro= int(input("Inroduce el diámetro del círculo: "))

area= round(math.pi * (diametro / 2) ** 2, 1)
perimetro= round(math.pi * diametro, 1)

print("El área de tu círculo es: ", area)
print("El perímetro de tu círculo es:", perimetro)
