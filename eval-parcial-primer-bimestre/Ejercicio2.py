x = float (input ("Ingrese el valor de x:"))
y = float (input ("Ingrese el valor de y:"))
z = float (input ("Ingrese el valor de z:"))

m = ((x + (y/z))) / ((x - (y/z)))

print(f"El valor de m, en base a las variables:\nx = %.1f\n\ty = %.1f\n\t\tz = %.1f\nda como resultado:\n\tm = %.1f\n" %(x,y,z,m) )
