#Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, 
# ofreciendo un descuento del 15% por la compra de más de 3 docenas y 10% en caso contrario. 
# Además, por la compra de más de 3 docenas se obsequia una unidad del producto por cada docena en exceso sobre 3. 
# Diseñe un programa que determine el monto de la compra, el monto del descuento, 
# el monto a pagar y el número de unidades de obsequio por la compra de cierta cantidad de docenas del producto.

cant_docenas = int(input("Cantidad de docenas: "))

precio_docena = 150

while True:
    try:
        cant_docenas = int(input("Ingrese la cantidad de docenas (o 0 para salir): "))

        if cant_docenas == 0:
            print("¡Gracias por su compra!")
            break

        if cant_docenas > 3:
            descuento = 0.15
            cantd_regalia = cant_docenas - 3
        else:
            descuento = 0.10
            cantd_regalia = 0

        compra = cant_docenas * precio_docena
        descuento_aplicado = compra * descuento
        total = compra - descuento_aplicado

        print("\nFACTURA")
        print("Monto de Compra: C$ ", compra)
        print("Monto del Descuento: C$ ", descuento_aplicado)
        print("Monto a Pagar: C$ ", total)
        print("Cantidad de producto de regalia: ", cantd_regalia)
        print("-" * 30)

    except ValueError:
        print("Por favor ingrese un número válido.")


