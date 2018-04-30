# Ingreso de datos
nota1 = float(input("Ingrese calificacion 1:"))
nota2 = float(input("Ingrese calificacion 2:"))
nota3 = float(input("Ingrese calificacion 3:"))
nota4 = float(input("Ingrese calificacion 4:"))

# Calculo de la media
media = (nota1 + nota2 + nota3 + nota4) / 4;

#Presentación de resultados
if media >= 90 and media <= 100: 
    print("El estudiante con el promedio de calificaciones %.2f ,tiene una puntuación de A." %media);
        
if media >= 80 and media <= 89:
    print("El estudiante con el promedio de calificaciones %.2f ,tiene una puntuación de B." %media);
    
if media >= 70 and media <= 79:
    print("El estudiante con el promedio de calificaciones %.2f ,tiene una puntuación de C." %media);

if media >= 0 and media <= 69:
    print("El estudiante con el promedio de calificaciones %.2f ,tiene una puntuación de D." %media);
