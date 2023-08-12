"""Práctica #6"""

def Promedio_Calificaciones():
    
    print("\n\nCalculadora de promedios \n")
    
    Calificaciones = []
   

    Verdad = True
    while Verdad == True:
        num = input("Número de asignaturas: ")
        if int(num) > 0 and num.isdigit():
            Verdad = False
        else:
            print("Ingresa un número válido.")
    
    num = int(num)
    
    for i in range(0, num):
        
        Verdad = True
        while Verdad == True:
            Calificacion = input("Ingresa la califiación múmero " + str(i + 1) + ": ")
            if Calificacion.isdigit() and int(Calificacion) >= 0 and int(Calificacion) <= 100:
                Verdad = False
            else:
                print("Ingresa un número válido.")
        
        Calificaciones.append(Calificacion)
    
    suma_de_calificaciones = 0
    
    for i in range(0, num):
        suma_de_calificaciones+= int(Calificaciones[i])
    
    promedio = suma_de_calificaciones / num
    
    if promedio >= 90:
        Calificacion_Final = "A"
    elif promedio >= 80:
        Calificacion_Final = "B"
    elif promedio >= 70:
        Calificacion_Final = "C"
    elif promedio >= 60:
        Calificacion_Final = "D"
    else:
        Calificacion_Final = "F"
        
    print("El promedio obtenido es: " + str(promedio) + "%\nLa nota obtenida es " + str(Calificacion_Final))

            
