print("Ingrese 3 letras Mayusculas si no las ingresa mayusculas el programa las transformara automaticamente a mayusculas\n")
uno = input("Ingrese la primera letra: ")
dos = input("Ingrese la segunda letra: ")
tres = input("Ingrese la tercera letra: ")

if uno < dos:
    orden = uno
else:
    orden = dos

primera = orden

if primera < tres:
    orden = primera
else:
    orden = tres

print()
print("LA PRIMERA LETRA QUE APARECE EN EL ABECEDARIO ES : ")
print(orden.upper())
