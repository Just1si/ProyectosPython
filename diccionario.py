diccionario = {
    "nombre" : "Isidoro",
    "apellido" : "Abad",
    "edad" : 34
}

print(diccionario)


# conjuntos: serie de elementos no ordenados y no repetidos (set en java)

conjunto = {1,2,3,4,}
print("Primer conjunto: ", conjunto)
conjunto.add(-1)
print("Conjunto añadido", conjunto)

def main():
      
    lista1 = ["Manzana", "Pera","Melocotón"]
    lista2 = ["Kiwi","Sandía","Melón"]
    lista1.extend(lista2)
    print(lista1[-1])

    tupla1 = (3,5,7)
    print(tupla1[0])
if __name__ == "__main__":
    main()