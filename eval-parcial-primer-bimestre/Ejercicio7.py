# Ingreso de datos
venta =float(input("ingrese el valor de las ventas de un empleado"))
sueldoFijo = 360.40
# Calculo del sueldo
if venta <= 500:
    porcentaje = 0.05 * venta
else:
    if venta > 500 and venta <= 1000:
        porcentaje = 0.08 * venta
    else: 
        if venta > 1000 and venta <= 5000:
            porcentaje = 0.10 * venta
        else:
            if venta > 5000:
                porcentaje = 0.15 * venta

sueldoFinal = sueldoFijo + porcentaje
# Presentación de resultados
print("El sueldo base del empleado es : 360.40 mas  su porcentaje de ventas es : %.2f " %porcentaje)
print("Sueldo final: %.2f " %sueldoFinal)
