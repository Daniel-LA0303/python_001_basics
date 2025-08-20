
#input siempre devuelve un string
nombre = input("Cual es tu nombre: ")

#podemos convertir el string a entero con int()
edad = int(input("Cual es tu edad: "))

#forma 1 de mostrar datos
print("Hola", nombre, "Bienvenido a Python", "Tu edad es", edad)

#foma 2 de mostrar datos
print("Hola {} Bienvenido a Python, Tu edad es {}".format(nombre, edad))

valorFlotante = float(input("Ingresa un valor flotante: "))


#Suma de dos numeros
print("Suma de dos numeros")
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
print("La suma es: ", num1 + num2)
