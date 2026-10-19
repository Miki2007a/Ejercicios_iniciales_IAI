#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales

numero_1 = float(input("Introduce el primer número: "))
numero_2 = float(input("Introduce el segundo número: "))

if numero_1 > numero_2:
    print("El primer número es mayor que el segundo.")
elif numero_1 < numero_2:
    print("El primer número es menor que el segundo.")
else:
    print("Los dos números son iguales.")