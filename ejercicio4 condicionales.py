# Ejercicio 4: Clasificación de Notas

# convertir a funciones

# Escribe un programa que solicite al usuario ingresar una puntuación (de 0 a 100) y luego muestre 
# una calificación de acuerdo con la siguiente escala:

#90-100: "A" (sobresaliente)
# 80-89: "B" (bueno)
#70-79: "C" (satisfactorio)
# 60-69: "D" (necesita mejorar)
# Menos de 60: "F" (reprobado)



def puntuacion_notas(puntuacion):
    if puntuacion_notas >=90:
        print("A-sobresaliente")
    elif puntuacion_notas >=80 and puntuacion_notas <89:
        print("B-bueno")
    elif puntuacion_notas >=70  and puntuacion_notas <79:
        print("C,satisfactorio")  
    elif puntuacion_notas>=60 and puntuacion_notas < 59:
        print("D-necesita mejorar")     
    else:
        print("F-reprobado") 
          
    puntuacion_notas()     
    



