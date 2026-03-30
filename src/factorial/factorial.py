import sys

if len(sys.argv) > 1:
    entrada = sys.argv[1]
else:
    entrada = input("Ingrese número o rango: ")

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

if "-" in entrada:
    partes = entrada.split("-")

    if partes[0] == "":  # -10
        desde = 1
        hasta = int(partes[1])
    elif partes[1] == "":  # 5-
        desde = int(partes[0])
        hasta = 60
    else:  # 4-8
        desde = int(partes[0])
        hasta = int(partes[1])

    for num in range(desde, hasta + 1):
        print(f"Factorial de {num} es {factorial(num)}")

else:
    num = int(entrada)
    print(f"Factorial de {num} es {factorial(num)}")

# Programa para calcular factoriales
# Permite ingresar:
# - Un número
# - Un rango (ej: 4-8)
# - Rangos abiertos (ej: -10 o 5-)