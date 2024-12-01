
#Booleanos

#True
bol1 = True

#False
bol2 = False

print(bol1, bol2)


#Metodos para booleanos

#Devuelve la cantidad mínima de bits necesarios para representar
# el número en binario, excluyendo el signo y los ceros a la izquierda.
numero = True
longitud_bits = numero.bit_length()
print(longitud_bits)  # Imprime 1

#Convierte un valor a un booleano. La mayoría de los valores
# se consideran True excepto False, None, 0 (y variantes como 0.0),
# y contenedores vacíos (como listas, diccionarios y conjuntos vacíos).
valor = 42
booleano = bool(valor)
print(booleano)  # Imprime True


#Devuelve True si todos los elementos
# del iterable son verdaderos (o si el iterable está vacío).
lista_verdadero = [True, True, True]
resultado = all(lista_verdadero)
print(resultado)  # Imprime True

lista_falso = [True, False, True]
resultado = all(lista_falso)
print(resultado)  # Imprime False

#any(iterable): Devuelve True si algún elemento
# del iterable es verdadero. Si el iterable está vacío, devuelve False.

lista_verdadero = [False, False, True]
resultado = any(lista_verdadero)
print(resultado)  # Imprime True

lista_falso = [False, False, False]
resultado = any(lista_falso)
print(resultado)  # Imprime False




