import math

print("Este programa puede resolver varios ejercicios matemáticos")
print("Elige el ejercicio que deseas realizar:")
print("1. Diagonal de un rectángulo")
print("2. Litros de pintura")
print("3. Distancia entre dos puntos")
print("4. Largo de una escalera")
print("5. Crecimiento de población")
opcion = int(input("Introduce el número del ejercicio: "))

if opcion == 1:
    print("Ejercicio 1: Diagonal de un rectángulo")
    ancho = float(input("Introduce el ancho del rectángulo: "))
    alto = float(input("Introduce el alto del rectángulo: "))
    diagonal = math.sqrt(ancho ** 2 + alto ** 2)
    print("La diagonal del rectángulo es:", diagonal)

elif opcion == 2:
    print("Ejercicio 2: Litros de pintura")
    areaPared = float(input("Introduce el área de la pared a pintar en m²: "))
    cantidadMaxima = float(input("¿Cuántos m² se cubren con 1 litro de pintura: "))
    pinturaNecesaria = areaPared / cantidadMaxima
    print("Necesitas", pinturaNecesaria, "litros de pintura")

elif opcion == 3:
    print("Ejercicio 3: Distancia entre dos puntos")
    x1 = int(input("Introduce la coordenada x del primer punto: "))
    y1 = int(input("Introduce la coordenada y del primer punto: "))
    x2 = int(input("Introduce la coordenada x del segundo punto: "))
    y2 = int(input("Introduce la coordenada y del segundo punto: "))

    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("distancia: ", distancia)

elif opcion == 4:
    print("Ejercicio 4: Largo de una escalera")

    alturaNecesaria = float(input("Introduce la altura que debe alcanzar la escalera: "))
    anguloNecesario = float(input("Introduce el ángulo que forma la escalera con el suelo (en grados): "))
    angulo = math.radians(anguloNecesario)
    largo = alturaNecesaria / math.cos(angulo)
    print("El largo de la escalera debe ser:", largo, "metros")

elif opcion == 5:
    print("Ejercicio 5: Crecimiento de población")
    Ni = int(input("Introduce la población inicial: "))
    t = int(input("Introduce el número de años: "))
    r = float(input("Introduce la tasa de crecimiento anual (en %): "))

    crecimiento = Ni * (math.e ** (r * t))
    print("La población después de", t, "años será:", round(crecimiento))