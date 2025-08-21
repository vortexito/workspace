import math

print("Este programa puede resolver varios ejercicios matemáticos")
print("Elige el ejercicio que deseas realizar:")
print("1. Área del triángulo")
print("2. Promedio de 4 materias")
print("3. 100 años")
print("4. Lustros")
print("5. Peso")
print("6. Pendiente de una recta")
print("7. Distancia recorrida por un caracol")
print("8. Costo teléfono")
print("9. Precio cemento")
print("10. Videojuegos")
option = int(input("Introduce el número del ejercicio: "))

if option == 1:
    print("Ejercicio 1: Área del triángulo")
    base = float(input("Introduce la base del triángulo: "))
    height = float(input("Introduce la altura del triángulo: "))
    area = (base * height) / 2
    print("El área del triángulo es:", area)

elif option == 2:
    print("Ejercicio 2: Promedio de 4 materias")
    subject1 = float(input("Introduce la calificación de la primera materia: "))
    subject2 = float(input("Introduce la calificación de la segunda materia: "))
    subject3 = float(input("Introduce la calificación de la tercera materia: "))
    subject4 = float(input("Introduce la calificación de la cuarta materia: "))
    promedio = (subject1 + subject2 + subject3 + subject4) / 4
    print("El promedio es:", round(promedio, 2))

elif option == 3:
    print("Ejercicio 3: 100 años")
    age = int(input("Introduce tu edad: "))
    actual_year = int(input("Introduce el año actual: "))
    year_100 = actual_year + (100 - age)
    print("Cumplirás 100 años en el año:", year_100)

elif option == 4:
    print("Ejercicio 4: Lustros")
    birth_year = int(input("Introduce tu año de nacimiento: "))
    current_year = int(input("Introduce el año actual: "))
    lustro = (current_year - birth_year) // 5
    print(lustro)
    
elif option == 5:
    print("Ejercicio 5: Peso")
    initial_weight = float(input("Introduce tu peso inicial en kg: "))
    final_weight = float(input("Introduce tu meta de peso en kg: "))
    months = int(input("Introduce el número de meses en los que lo quieres lograr: "))
    monthly_loss = (initial_weight - final_weight) / months
    print("Debes perder", round(monthly_loss, 2), "kg por mes para alcanzar tu meta.")

elif option == 6:
    print("Ejercicio 6: Pendiente de una recta")
    x1 = float(input("Introduce la coordenada x del primer punto: "))
    y1 = float(input("Introduce la coordenada y del primer punto: "))
    x2 = float(input("Introduce la coordenada x del segundo punto: "))
    y2 = float(input("Introduce la coordenada y del segundo punto: "))
    pendiente = (y2 - y1) / (x2 - x1)
    print("La pendiente de la recta es:", pendiente)

elif option == 7:
    print("Ejercicio 7: Distancia recorrida por un caracol")
    minutes = int(input("Introduce el número de minutos que recorrerá el caracol: "))
    speed = 5.7 # velocidad en mm/s
    distance = minutes * 60 * speed
    print("El caracol recorrerá", distance, "mm en", minutes, "minutos.")

elif option == 8:
    print("Ejercicio 8: Costo teléfono")
    price = 0.80 #for message, mega or minute
    messages = int(input("Introduce el número de mensajes enviados: "))
    megas = int(input("Introduce el número de megas consumidos: "))
    phone_minutes = int(input("Introduce el número de minutos de llamada: "))
    total_cost = (messages + megas + phone_minutes) * price
    print("El costo mensual es de:", round(total_cost, 2), "pesos.")

elif option == 9:
    print("Ejercicio 9: Precio cemento")
    cement_bag_cuantity = int(input("Introduce la cantidad de bolsas de cemento: "))
    price_per_bag = int(input("Introduce el precio por bolsa de cemento: "))
    price_before_taxes = cement_bag_cuantity * price_per_bag
    print("El precio antes de impuestos es:", price_before_taxes, "pesos.")
    taxes = 0.16
    print("Impuestos:", round(price_before_taxes * taxes, 2), "pesos.")
    print("El precio total es:", round(price_before_taxes * (1 + taxes), 2), "pesos.")

elif option == 10:
    print("Ejercicio 10: Videojuegos")
    new_games = int(input("Introduce el número de videojuegos nuevos: "))
    used_games = int(input("Introduce el número de videojuegos usados: "))
    new_game_price = 1000
    used_game_price = 350
    total_cost = (new_games * new_game_price) + (used_games * used_game_price)
    print("El costo total de los videojuegos es:", total_cost, "pesos.")
    
else:
    print("Opción no válida. Por favor, elige un número entre 1 y 10.")