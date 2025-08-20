

#Metodos de cadenas

mensaje = "Hola, mundo!"
longitud = len(mensaje)
print(longitud)  # Imprime 13

#Impresion de la cadena en minusculas
resultado = mensaje.lower()
print(resultado)  # Imprime "hola, mundo!"

#Impresion de la cadena en mayusculas
resultado2 = mensaje.upper()
print(resultado2)  # Imprime "HOLA, MUNDO!"

#Impresion de la cadena con la primera letra en mayuscula
resultado3 = mensaje.capitalize()
print(resultado3)  # Imprime "Hola, mundo!"

#Impresion de la cadena con cada palabra en mayuscula
mensaje = "Hola, hola, hola!"
conteo = mensaje.count("hola")
print(conteo)  # Imprime 3

#Devuelve el índice de la primera ocurrencia de una subcadena.
# Si no encuentra la subcadena, devuelve -1.
mensaje = "Hola, mundo!"
indice = mensaje.find("mundo")
print(indice)  # Imprime 7

#Reemplaza todas las ocurrencias de una subcadena con otra.
mensaje = "Hola, mundo!"
nuevo_mensaje = mensaje.replace("mundo", "Python")
print(nuevo_mensaje)  # Imprime "Hola, Python!"

#Divide la cadena en una lista de subcadenas utilizando el separador especificado.
mensaje = "Hola, mundo!"
partes = mensaje.split(", ")
print(partes)  # Imprime ['Hola', 'mundo!']

#Elimina los espacios en blanco al principio y al final de la cadena.
mensaje = "   Hola, mundo!   "
resultado = mensaje.strip()
print(resultado)  # Imprime "Hola, mundo!"

#Pone en mayusculas la primera letra de cada palabra
print(mensaje.title())





