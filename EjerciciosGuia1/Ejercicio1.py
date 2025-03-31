#Desarrolla un programa que calcule el importe a pagar por un vehículo al circular por una autopista. 
# El vehículo puede ser una bicicleta, una moto, un carro o un camión. Para definir el conjunto de vehículos deben utilizar 
# una estructura adecuada. El importe se calculará según los siguientes datos:
#a) Un importe fijo de 100 córdobas para la bicicleta.
#b) Las motos y los carros pagarán 30 córdobas por Km.
#c) Los camiones pagarán 30 córdobas por Km. más 25 córdobas por toneladas.

print("Menu de vehiculos: ")
print("1. Bicicleta")
print("2. Motos y carros")
print("3. Camiones")

tipo_vehiculo = int(input("Escriba el numero de tipo de vehiculo: "))

importe = 30
toneladas = 25

if tipo_vehiculo == 1:
    importe = 100
    print("Importe a pagar es de: ", importe)
elif tipo_vehiculo == 2:
    cantidad_km = float(input("Cantiad de Km: "))
    print("Importe a pagar es de: ", cantidad_km * importe)
elif tipo_vehiculo == 3:
    cantidad_km = float(input("Cantiad de Km: "))
    cantidad_ton = float(input("Cantiad de Toneladas: "))
    
    print("Importe a pagar es de: ", cantidad_km * importe)