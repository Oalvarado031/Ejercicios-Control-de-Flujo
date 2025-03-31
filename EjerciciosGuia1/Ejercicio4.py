#Diseñe un programa que lea un número de tres cifras y determine si es igual al revés del número.

while True:
    numero = input("Ingrese un número de tres cifras: ")

    # Verifiación quee tenga tres cifras y que sea numérico
    if numero.isdigit() and len(numero) == 3:
        break
    else:
        print("Entrada inválida. Por favor ingrese un número de TRES cifras.")

# Se invierte el número
numero_invertido = numero[::-1]

# Salida
if numero == numero_invertido:
    print("El número es igual al revés.")
else:
    print("El número NO es igual al revés.")
