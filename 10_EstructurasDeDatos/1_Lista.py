
#La lista es el array de python
#Las listas son mutables

lista = ["elemento1", "elemento2", "elemento3"]
print(lista) #Imprime la lista completa
print(lista[0]) #Imprime el primer elemento de la lista

#metodos de las listas
print(len(lista)) #Imprime la longitud de la lista

print(lista.append("elemento4"))#Agrega un elemento al final de la lista

print(lista.insert(0, "elemento0"))#Agrega un elemento en la posicion indicada y recorrere

print(lista.remove("elemento0")) #Elimina el elemento indicado

print(lista.pop())  #Elimina el ultimo elemento de la lista

print(lista.count("elemento1")) #
print(lista.index("elemento2")) #Devuelve el indice del elemento indicado
print(lista.clear()) #Elimina todos los elementos de la lista


'''
#debanado de listas
print(lista[0:2]) #Imprime los elementos de la posicion 0 a la 2
print(lista[2:]) #Imprime los elementos de la posicion 2 hasta el final
print(lista[:2]) #Imprime los elementos desde el inicio hasta la posicion 2
print(lista[-1]) #Imprime el ultimo elemento de la lista

'''

#llenando una lista
lista2 = []

for i in range(5):
    num = int(input("Ingresa un numero: "))
    lista2.append(num)

print(lista2)
