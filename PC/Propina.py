print("Este programa calcula la propina que debes dejar")

porcentajeProppina = float(input("¿Qué porcentaje de propina deseas dejar?"))
cuenta = float(input("¿Cuál es el total de la cuenta?"))

propina = (porcentajeProppina / 100) * cuenta
total = cuenta + propina

print("La propina que debes de dejar es:", round(propina, 2), "$")