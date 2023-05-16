def calcular_descuento(precio, porcentaje_descuento):
    descuento = precio * (porcentaje_descuento / 100)
    precio_con_descuento = precio - descuento
    return precio_con_descuento

precio = 100
porcentaje_descuento = 20
precio_con_descuento = calcular_descuento(precio, porcentaje_descuento)
print(precio_con_descuento)