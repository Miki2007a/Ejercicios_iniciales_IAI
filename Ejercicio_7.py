#7. programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?

variable1 = float(input("Introduce el primer número: "))
variable2 = float(input("Introduce el segundo número: "))   

print("Suma:", variable1 + variable2)   
print("Resta:", variable1 - variable2)
print("Multiplicación:", variable1 * variable2)     
print("División:", round(variable1 / variable2, 2)) 
print("División entera:", variable1 // variable2)
print("Residuo:", variable1 % variable2)
print("Potencia:", variable1 ** variable2)  