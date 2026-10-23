#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
letra = input("Introduce una letra: ")

if letra. isalpha() and len(letra) == 1:
    if letra.isupper():
        print(f"La letra {letra} está en mayúscula.")
    else:
        print(f"La letra {letra} no está en mayúscula.")
else:
    print("La entrada no es una letra válida.")