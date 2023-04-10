
#Importamos librerias

import numpy as np
import math
from matplotlib import pyplot as plt

# Creamos una funcion auxiliar que verifique que N sea un natural
def esNatural(N, func):
    if type(N)==int and N>=0:
        return N
    else:
        newN = int(input("Favor ingresar un número natural (con cero incluido):" ))
    return func(newN)

# Creamos una funcion para que redondee L al numero natural de arriba.
def redondeo(n):
    n1 = math.floor(n) + 1
    return n1

# Creamos una funcion para saber si es par o impar, si es par (n) que devuelva n+1 (impar).
def esImpar(n):
    if n % 2 == 0:
        return n + 1
    else:
        return n

# Creamos una funcion auxiliar para calcular las dimensiones del tablero (LxL) y que L sea impar para que tenga centro.
def dimensionTablero(N):
    pi = math.pi
    L1 = math.sqrt(N/pi) + 1
    L2 = redondeo(L1)
    L3 = esImpar(L2)
    tablero = np.zeros([L3, L3], dtype = int)
    return tablero, L3

def derrumbeCelda(x, y, tablero):
    while tablero[x, y] >= 4:
        tablero[x, y] -= 4
        tablero[x + 1, y] += 1
        tablero[x - 1, y] += 1
        tablero[x, y + 1] += 1
        tablero[x, y - 1] += 1
    return tablero


def arena(N):
  # escriba su código aquí
  x = esNatural(N, arena)
  tablero, L = dimensionTablero(x)
  centro = int((L - 1)/2)
  tablero[centro, centro] = x
  while any(cell <= 4 for fila in tablero for cell in fila):
    for y in range(0, L-1):
      for x in range(0, L-1):
        tablero = derrumbeCelda(x, y, tablero)


  
        
  return tablero

print(arena(128))

