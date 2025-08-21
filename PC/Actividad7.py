print("Ejercicio 1")
number = int(input("Introduce un número entero: "))
if number % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

if number < 0:
    print("El número es negativo.")
elif number > 0:
    print("El número es positivo.")

print("Ejercicio 2")
x = int(input("Introduce el valor de x: "))
y = int(input("Introduce el valor de y: "))
z = int(input("Introduce el valor de z: "))

triangle = False

if x + y > z or x + z > y or y + z > x:
    triangle = True    

if triangle == True:
    if x == y and y == z:
        print("Es un triangulo equilátero.")
    if x == y or y == z or x == z:
        print("Es un triángulo isósceles.")
    if x != y and y != z and x != z:
        print("Es un triángulo escaleno.")
else:
    print("No es un triángulo.")
