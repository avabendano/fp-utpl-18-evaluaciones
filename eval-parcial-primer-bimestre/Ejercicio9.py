# Ingreso de datos de triangulo 1
print("Ingrese datos del triangulo 1:\n")
lado1 = float (input ("Ingrese lado 1 del triangulo:"))
lado2 = float (input ("Ingrese lado 2 del triangulo:"))
lado3 = float (input ("Ingrese lado 3 del triangulo:"))
ang1 = float (input ("Ingrese angulo 1 del triangulo:"))
ang2 = float (input ("Ingrese angulo 2 del triangulo:"))
ang3 = float (input ("Ingrese angulo 3 del triangulo:"))
# Ingreso de datos de triangulo 2
print("Ingrese Datos del triangulo 2:\n")
lado11 = float (input ("Ingrese lado 1 del triangulo:"))
lado22 = float (input ("Ingrese lado 2 del triangulo:"))
lado33 = float (input ("Ingrese lado 3 del triangulo:"))
ang11 = float (input ("Ingrese angulo 1 del triangulo:"))
ang22 = float (input ("Ingrese angulo 2 del triangulo:"))
ang33 = float (input ("Ingrese angulo 3 del triangulo:"))
# Presentacion de resultados
if lado1 == lado11 and lado2 == lado22 and lado3 == lado33 and ang1 == ang11 and ang2 == ang22 and ang3 == ang33:
    print("Los triangulos SON CONGRUENTES")
else:
    print("Los triangulos NO SON CONGRUENTES")
       
