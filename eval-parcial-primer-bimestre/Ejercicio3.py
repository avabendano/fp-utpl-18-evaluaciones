s = int( input ("Ingrese los segundos:"))

hora = s / 3600

minuto = (s -(3600 * hora)) / 60
segundo = s - ((hora * 3600) + (minuto * 60))
print("%d segundos es igual a :" %s);
print("%s hr %s min %s seg"%(hora,minuto,segundo));

