"""Función 4"""

""" Esta función se diseñó para realizar 4 diferentes operaciones 
  (suma, resta, multiplicación y división)."""



def Calculadora(a,b):
    Falso = False
    print('1.- Suma \n'
    '2.- Resta \n'
    '3.- Multiplicación \n'
    '4.- División \n') 
    while Falso == False: 
        Operacion = input('¿Qué operación desea realizar? ')
        
        if Operacion.isdigit() and int(Operacion) > 0 and int(Operacion) < 5:
            Falso = True
        else: 
            print('Ingresa un número valido.')
    
    Operacion = int(Operacion)
    if Operacion == 1:
        Resultado = a + b
    elif Operacion == 2: 
        Resultado = a - b
    elif Operacion == 3: 
        Resultado = a * b
    else: 
        Resultado = a / b
  
    Resultado = 'Tu resultado es ' + str(Resultado)
    
    return Resultado