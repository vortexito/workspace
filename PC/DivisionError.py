num1 = float(input("Introduce el primer número de la división:"))
num2 = float(input("Introduce el segundo número de la división:"))
if num2 == 0:
    print("Error: No se puede dividir por cero.")
else:
    result = num1 / num2
    print("El resultado de la división es:", result)