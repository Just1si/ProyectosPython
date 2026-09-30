# como se usan las estructuras de control en python
## Estructuras de control: if, for, while

## Estructura if
print("Estructura if e if-else")
if(True):
    print("La condición es verdadera")
    #a diferencia de java no se usan llaves 
    # para delimitar el bloque de código,
    #  sino que se usa la indentación

    #estructura if-else
if(False):
    print("La condición es verdadera")
else:
    print("La condición es falsa") 
    #similar a java, se puede usar la estructura if-elif-else

### Estructura for
print("Estructura for")
print("Iterando del 1 al 4")
for i in range(1,5): 
    print(i)
    #en python no se usa la palabra reservada "for" para declarar un bucle for, 
    # sino que se usa la palabra reservada "for" seguida de una variable y la función range()
    #  que genera una secuencia de números enteros

    #tambien se puede usar la estructura 
    # for para iterar sobre una lista

print("Iterando sobre una lista de juegos")
for juego in ["FIFA", "Mortal Kombat", "GTA"]:
        print(juego)

# puede también generar estructuras similares a los objetos en java
# dentro de estas listas, aunque sin ser objetos, es decir, 
# son diccionarios, que son estructuras de datos que permiten 
# almacenar pares de clave-valor

print("Iterando sobre una lista de diccionarios")
for juego in [
    {
        "nombre": "FIFA",
        "genero": "Deportes",
        "año": 2020,
        "precio": 59.99
    },{
        "nombre"
          : "Mortal Kombat",
        "genero": "Lucha",
        "año": 2019,
        "precio": 49.99
    },{
        "nombre": "GTA",
        "genero": "Acción",
        "año": 2018,
        "precio": 39.99
    },{
        "nombre": "The Last of Us",
        "genero": "Aventura",
        "año": 2020,
        "precio": 59.99
    }]:
    print(juego)


### Estructura while
print("Estructura while")
print("Iterando del 1 al 4")
i = 1
while(i < 5):
    print(i)
    i += 1  # en contraste con java, 
            # en python no se usan los operadores ++ o -- 
            # para incrementar o decrementar una variable,
            # sino que se usa el operador += o -=

