

#bucle for
for i in range(5):
    #instrucciones
    print("Hola")


lista = ["elemento1", "elemento2", "elemento3"]
for i in lista:
    print(i)

#recorrer de manera inversa
for i in range(10, 0, -1):
    print(i)


#continue y break
for i in range(10):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
