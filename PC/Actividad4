import math

print("Este programa puede resolver varios ejercicios matemáticos")
print("Elige el ejercicio que deseas realizar:")
print("1. Longitud del cateto opuesto")
print("2. Área y volumen de una esfera")
print("3. Área de un triángulo")
opcion = int(input("Introduce el número del ejercicio: ")) 


if opcion == 1:
    print("Ejercicio 1, calcula la longitud del cateto opuesto")
    hipotenusa = float(input("Introduce la longitud de la hipotenusa: "))

    grados = math.radians(30)

    catetoOpuesto = math.sin(grados) * hipotenusa
    print("La longitud del cateto opuesto es:", catetoOpuesto)

elif opcion == 2:
    print("Ejercicio 2, calcula el área y volumen de una esfera")
    radio = float(input("Introduce el radio de la esfera: "))
    area = 4 * math.pi * radio ** 2
    volumen = (4/3) * math.pi * radio ** 3
    print("El área de la esfera es:", area)
    print("El volumen de la esfera es:", volumen)

elif opcion == 3:
    print("Ejercicio 3, calcula el área de un triángulo")
    a = float(input("Introduce el lado a del triángulo: "))
    b = float(input("Introduce el lado b del triángulo: "))
    c = float(input("Introduce el lado c del triángulo: "))

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("El área del triángulo es:", area)