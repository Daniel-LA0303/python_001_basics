

edad = int(input("Cual es tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#Elif
numero = int(input("Ingresa un numero: "))
if numero > 0:
    print("El numero es positivo")
elif numero == 0:
    print("El numero es cero")
else:
    print("El numero es negativo")

#Condicionales anidados
numero = int(input("Ingresa un numero: "))

if numero >= 0:
    if numero == 0:
        print("El numero es cero")
    else:
        print("El numero es positivo")
else:
    print("El numero es negativo")


