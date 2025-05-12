# # Aca hay un comentario 
# if 3 > 5:
#     print("Esto no se imprime")

# if 5 > 3: # Aca va otro un comentario 
#     print("5 es mayor a 3")

# x = 5
# y = "Chanchitos"

# print(x, y)


# email = "chanchito@feliz.com"

# print (email)

# miVar = "chanchito"

# a, b, c, = "lala", "lele", "lili"
# print(a, b, c)

# val1 = val2 = val3 ="chanchito feliz"
# print(val1, val2, val3)

# inicio = "hola "
# final = "mundo"

# print(inicio + final)

# palabra = "hola mundo"

# entero = 23 
# conDecimales = 15.5
# complejos = 1j

# print(palabra, entero, conDecimales, complejos)

lista = ["hola mundo", "lala", "lele"]
lista2 = lista.copy()
lista.append("peo")
# lista.clear()

# print(lista, lista2.count(3))
# print(len(lista), len(lista2))
largoLista = len(lista)
largoLista2 = len(lista2)

# print(largoLista,largoLista2)

# print(lista[0])

# lista.pop()
# lista.pop() #elimina el ultimo elemento 
# lista.remove("hola mundo") #este elimina un elemento de una lista 

lista.reverse() #da vuelta el orden de la lista 
lista.sort() #ordenar una lista pero deben tener los mismos tipos de datos, str, int, float, etc.
tupla = ("hola", "mundo", "somos", "tuplas")
listaTupla = list(tupla)
listaTupla.append("chanchito")
print(listaTupla)

rango = range(6)
# print(rango)

diccionario = {
    "nombre": "chanchito feliz",
    "raza": "Persa",
    "edad": 5
}
print(diccionario)

