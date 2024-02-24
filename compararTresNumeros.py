n1 = int(input("Ingrese numero1: "))
n2 = int(input("Ingrese numero2: "))
n3 = int(input("Ingrese numero3: "))

if n1 > n2 and n1 > n3:
    print("El numero ", n1, " es el mayor")

elif n2 > n1 and n2 > n3:
    print("El numero ", n2, " es el mayor")

elif n3 > n2 and n3 > n1:
    print("El numero", n3, "es el mayor")

else:
    print("Los 3 numeros son iguales")