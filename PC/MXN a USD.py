print("Este programa convierte pesos mexicanos a dólares estadounidenses o viceversa")
print("¿Quieres convertir de pesos a dólares (1) o de dólares a pesos (2)?")

opcion = int(input())

if opcion == 1:
    print("Has elegido convertir de pesos a dólares.")
    
    tasa_cambioUSD = float(input("¿Cuál es la tasa de cambio actual?"))
    mxn = float(input("¿Cuántos pesos mexicanos tienes? "))

    usd = mxn / tasa_cambioUSD
    print("Tienes", round(usd, 2), "dólares estadounidenses")

elif opcion == 2:
    print("Has elegido convertir de dólares a pesos.")

    tasa_cambioMXN = float(input("¿Cuál es la tasa de cambio actual?"))
    usd = float(input("¿Cuántos dólares estadounidenses tienes? "))

    mxn = usd * tasa_cambioMXN
    print("Tienes", round(mxn, 2), "pesos mexicanos")