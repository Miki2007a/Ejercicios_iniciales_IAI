#30. . Realiza un programa que controle si la longitud de una frase introducida por teclado es igual, menor o mayor de 11 caracteres. Utiliza elif 

frase = input("Introduce una frase: ")

if len(frase) < 11:
    print(f"La longitud de la frase es menor que 11 caracteres, tiene {len(frase)} caracteres.")
elif len(frase) == 11:
    print(f"La longitud de la frase es de 11 caracteres")
else:
    print(f"La longitud de la frase es mayor que 11 caracteres, tiene {len(frase)} caracteres.")