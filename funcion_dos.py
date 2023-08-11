'''Función 2'''

""" Esta función se diseñó para reacomodar en 
    sentido contrario los elementos de una lista en Python. """
    
def Vectores(n):
    n = int(n) + 1
    J = n//2
    lista = list(range(1,n))
    print(lista)
    for i in range(0,J): 
        inter = lista[n - 2]
        lista[n - 2] = lista[i]
        lista[i] = inter
        n = n - 1
    return lista
