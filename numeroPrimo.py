num = int(input("Ingrese numero: "))

if num > 1:
    for a in range(2, int(num ** 0.5) + 1):
        if num % a == 0:
            print(num, "no es un numero primo")
            break
    else:
        print(num, "es un numero primo")

else: print(num, "no es un numero primo")