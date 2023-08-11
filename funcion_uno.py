'''Función 1'''

""" Esta función se diseñó para realizar la suma de todos los números de característica 
    par en determinado rango de números.""" 

def SumarPares(n,m):
    suma = 0 
    while n <= m: 
        if n % 2 != 0:
            n = n + 1
        suma = suma + n
        n = n + 2
    return suma