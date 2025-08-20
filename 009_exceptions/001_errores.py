



try:
    edad = int(input("Cual es tu edad: "))
    print("Tu edad es: ", edad)
except:
    print("Error al ingresar la edad")


#Multiples Excepciones

try:
    edad = int(input("Cual es tu edad: "))
    print("Tu edad es: ", edad)
    print(10/0)
except ValueError:
    print("Error al ingresar la edad")
except ZeroDivisionError:
    print("No se puede dividir entre 0")

