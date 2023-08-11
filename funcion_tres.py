'''Función 3'''

""" Esta función se diseñó para determinar si un número es primo o no. """

def EsPrimo(K):
    Resul = True
    Primo = 2
    while Primo < K:
        if K % Primo == 0:
            Resul = False
            Primo = K + 1
        else: 
            Primo = Primo + 1
    return Resul

