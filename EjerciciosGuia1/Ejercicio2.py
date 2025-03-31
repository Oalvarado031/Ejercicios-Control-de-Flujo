# Escribir un programa que permita emitir la FACTURA correspondiente, a una compra 
# de un artículo determinado, del que se adquieren una o varias unidades.
# El IVA a aplicar es de 15% y si el Sub Total (precio de venta por cantidad), 
# es mayor de 1000, se aplicará un descuento del 12%.

precio_unidad = 125

#entrada
cant_unidades = int(input("Cantidad de Articulos: "))


#calculos
subtotal = precio_unidad * cant_unidades
iva = subtotal * 0.15
total = subtotal +iva
descuento = total * 0.12


#salida
print("FACTURA")
print("-------")
print("Precio por unidad : C$ ",precio_unidad)
print("Cantidad de Unidades: ",cant_unidades)
print("Subtotal   : C$",subtotal)
print("IVA 15% : C$ ", iva)
print("Total: C$ ", total)

if total > 1000:
    print("Aplica a descuento")
    print("Total con descuento: C$ ", total - descuento)
    