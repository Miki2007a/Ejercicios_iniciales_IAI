#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.

precio_entrada = 12

menores = int(input("Introduce el número de menores de 18 años: "))
adultos = int(input("Introduce el número de adultos: "))

total_menores = menores * precio_entrada * 0.5
total_adultos = adultos * precio_entrada * 0.9

total_a_pagar = total_menores + total_adultos

print("Total a pagar por los menores de 18 años:", total_menores)
print("Total a pagar por los adultos:", total_adultos)
print("El total a pagar es:", total_a_pagar)