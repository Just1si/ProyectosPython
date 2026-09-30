# 1. pedir al usuario una nota numerica entera y decir
# si la nota es suficiente o no, siendo suficiente una nota mayor o igual a 5
# realizar una version con if y otra con match-case

print("Ingrese una nota numerica entera: ")

nota = int(input())


print("-- Version con if-elif-else --")

if(nota < 5):
    print("Insufuciente")
elif(nota < 6):
    print("La nota es Suficiente")
elif(nota < 7):
    print("La nota es Bien")
elif(nota < 9):
    print("La nota es Notable")
else:
    print("La nota es Sobresaliente")


print("-- Version con match-case --")
match nota:
    case n if n < 5:
        print("Insuficiente")
    case n if n < 6:
          print("La nota es Suficiente")  
    case n if n == 6:
        print("La nota es Bien")
    case n if n >= 7 and n <= 8:
        print("La nota es Notable")
    case n if n >= 9 and n <= 10:
        print("La nota es Sobresaliente")

#2. Pedir al usuario dos valores por panntalla:
# el precio de un producto (en float) y el tipo de IVA (General, Reducido o Superreducido) 
# y mostrar el precio final del producto con IVA incluido.
# Realizar una versión con if y otra con match-case

print("Ingrese el precio del producto: ")
precio = float(input())
print("Ingrese el tipo de IVA (General, Reducido o Superreducido): ")
tipo_iva = input()

print("-- Version con if-elif-else --")
if(tipo_iva == "General"):
    precio_final = precio * 1.21
elif(tipo_iva == "Reducido"):  
    precio_final = precio * 1.10
elif(tipo_iva == "Superreducido"):
    precio_final = precio * 1.04
else:
    print("Tipo de IVA no válido")

print("El precio final del producto con IVA incluido es: ", precio_final)

print("-- Version con match-case --")
match tipo_iva:
    case "General":
        precio_final = precio * 1.21
    case "Reducido":
        precio_final = precio * 1.10
    case "Superreducido":
        precio_final = precio * 1.04

    # Caso por defecto(a diferencia de java no se pone default sino _, ni tamppoco se pone break)
    case _:
        print("Tipo de IVA no válido")

print("El precio final del producto con IVA incluido es: ", precio_final)

# 3. Pedir al usuario la edad de una persona
# y decir si es mayor o menor de edad. En caso de que la edad
# sea negativa, mostrar un mensaje de error.
# Si la edad es mayor o igual a 120 indicar que es un vampiro

print("Ingrese la edad de la persona: ")
edad = int(input())

match edad:
    case n if n < 0:
        print(f"Error: La edad no puede ser negativa: {edad}")
    case n if n <= 18:
        print("La persona es menor de edad")
    case n if n < 120:
        print("La persona es mayor de edad")
    case n if n >= 120:
        print("La persona es un vampiro y se debe traer ajo")   

# 4. A partir de 60mm en 12 horas se declara alerta amarilla
# a partir de 120 mm alerta roja. Mostrar si no hay aletra o el tipo de alerta
# pidiendole los datos al usuario. REALIZAR CON IF Y CON MATCH

print("Introduzca cuanta lluvia ha precipitado en las últimas 12 horas:")
lluvia = int(input())

if (lluvia <= 0):
    print("No hay alerta")
elif(lluvia >= 60):
    print("Alerta amarilla")
elif(lluvia >= 120):
    print("Alerta roja")


print("Vuelva a introducir cuanta lluvia ha caido en las últimas 12 horas")
lluvia2 = int(input())

match lluvia2:
    case x if x <= 0:
        print("Sin alerta")
    case x if x <= 60:
        print("Alerta amarilla")
    case x if x >= 120:
        print("Alerta roja")