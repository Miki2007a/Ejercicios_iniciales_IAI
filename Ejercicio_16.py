#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso (raíz y división).

import math

numero = float(input("Introduce un número: "))

raiz = round(math.sqrt(numero), 2)
division = int(raiz // 2)

print("Raíz cuadrada:", raiz)
print("Raíz cuadrada dividida entre 2:", division)

