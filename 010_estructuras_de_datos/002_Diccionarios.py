
diccionario = {}

diccionario["nombre"] = "Codi"
diccionario["edad"] = 27
diccionario["estatura"] = 1.70
diccionario["provincia"] = "CCDMX"
diccionario["telefono"] = "1234567890"

print(diccionario)


#metodos de los diccionarios
print(diccionario.keys()) #muestra las llaves
print(diccionario.values()) #muestra los valores
print(diccionario.items()) #muestra los elementos
print(diccionario.get("nombre")) #muestra el elemento de la llave indicada
print(diccionario.update({"nombre":"Nuevo"})) #actualiza el valor de la llave indicada
print(diccionario.pop("nombre")) #elimina el elemento de la llave indicada
print(diccionario.popitem()) #elimina el ultimo elemento


print(diccionario.clear()) #elimina todos los elementos del diccionario
