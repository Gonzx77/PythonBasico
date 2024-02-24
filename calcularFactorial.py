numero = int(input("Ingrese numero a factorizar: "))

factorial = 1
a = 1
while a <= numero:
    factorial *= a
    a += 1

print("El resultado es", factorial)