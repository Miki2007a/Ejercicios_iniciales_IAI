#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógico

nota = float(input("Introduce tu nota: "))

if nota < 0 or nota > 10:
    print("La nota introducida no es válida. Debe estar entre 0 y 10.")
elif nota >= 8.5:
    print(f"La nota que has sacado es {nota}, por lo tanto es excelente.")
elif nota >= 6.5:
    print(f"La nota que has sacado es {nota}, por lo tanto es notable.")
elif nota >= 5:
    print(f"La nota que has sacado es {nota}, por lo tanto es satisfactorio.")
else:
    print(f"La nota que has sacado es {nota}, por lo tanto es insuficiente.")