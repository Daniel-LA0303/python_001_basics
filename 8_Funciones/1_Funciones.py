import math
import random

#funciones
def suma(a,b):
    return a + b

print(suma(5,5))


def tabla():
    for i in range(10):
        print("7 x {} = {}".format(i, 7*i))


tabla()

# math y sus funciones
print(math.pi)
print(math.e)
print(math.sin(90))
print(math.pow(2,3))
print(math.sqrt(25))
print(math.floor(9.8))
print(math.ceil(9.8))
print(math.trunc(9.8))
print(math.factorial(5))
print(math.fabs(-5))

# random y funciones
print(random.random())
print(random.randint(1,100))
print(random.randrange(1,100,2))
print(random.choice(["Hola","Adios","Hasta luego"]))
print(random.choice("Hola"))
