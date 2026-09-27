#13. Realiza un programa que, a partir introducir el lado de un cubo, presente por pantalla el área y para calcular el volumen utiliza el operador de exponente.

lado = float(input("Introduce el valor del lado del cubo: "))
area = 6 * (lado * lado)
volumen = lado * lado * lado

print("Área:", area)
print("Volumen:", volumen)
