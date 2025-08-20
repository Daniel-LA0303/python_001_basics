#En las tuplas no se pueden modificar los elementos
tupla = (1,2,3,4,5,6,7,8,9,0)

print(tupla)
print(tupla[0]) #imprime el primer elemento
print(tupla[-1]) #imprime el ultimo elemento
print(tupla[0:2]) #imprime los elementos de la posicion 0 a la 2
print(tupla[2:]) #imprime los elementos de la posicion 2 hasta el final
print(tupla[:2]) #imprime los elementos desde el inicio hasta la posicion 2

#strude
print(tupla[::2])  # Resultado: (1, 3, 5, 7, 9) de 2 en 2
print(tupla[::-1]) # Resultado: (0, 9, 8, 7, 6, 5, 4, 3, 2, 1) de derecha a izquierda
print(tupla[2:8:3])  # Resultado: (3, 6) desde la posición 2 hasta la 8 de 3 en 3
print(tupla[9:2:-3])  # Resultado: (0, 7, 4) desde la posición 9 hasta la 2 de 3 en 3

