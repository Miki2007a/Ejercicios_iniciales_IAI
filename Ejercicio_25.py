#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.

nota = float(input("Introduce tu nota: "))

if nota < 0 or nota > 10:
    print("La nota introducida no es válida. Debe estar entre 0 y 10.")
elif nota >= 8.5 and nota <= 10:
    print(f"La nota que has sacado es {nota}, por lo tanto es excelente.")
elif nota >= 6.5 and nota < 8.5:
    print(f"La nota que has sacado es {nota}, por lo tanto es notable.")
elif nota >= 5 and nota < 6.5:
    print(f"La nota que has sacado es {nota}, por lo tanto es satisfactorio.")
else:
    print(f"La nota que has sacado es {nota}, por lo tanto es insuficiente.")