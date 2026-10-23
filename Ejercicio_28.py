#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.

letra = input("Introduce una letra: ")

if letra. isalpha() and len(letra) == 1:
    if letra.isupper():
        print(f"La letra {letra} está en mayúscula.")
    else:
        print(f"La letra {letra} no está en mayúscula.")
elif letra. isdigit():
    print("La entrada es un número.")
else:
    print("La entrada es un símbolo.")
