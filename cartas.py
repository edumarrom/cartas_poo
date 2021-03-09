# ¿Traerme funciones del repartidor aquí?
from random import shuffle as mezclar
"""
# Cartas.
- Las cartas son 4:
    - 0. Gran Éxito: + 2 de vida.
    - 1. Éxito: + 1 de vida.
    - 2. Fracaso: - 1 de vida.
    - 3. Gran Fracaso: - 2 de vida.
"""

GE,E, F, GF = range(4)
baraja = [GE,   # = 0
          E,    # = 1
          F,    # = 2
          GF    # = 3
          ]

def mostrar():
    """Crea una copia de la baraja identificándola con sus siglas."""
    mano = []
    for carta in baraja:
        if carta == GE:
            mano.append('[GE]')
        elif carta == E:
            mano.append('[E]')
        elif carta == F:
            mano.append('[F]')
        elif carta == GF:
            mano.append('[GF]')
    print('\n', mano, '\n')

def barajar():
    """Baraja las cartas de forma aleatoria."""
    mezclar(baraja)
    print('(El repartidor mezcla las cartas cuidadosamente.)')

def carta(seleccion):
    return baraja[seleccion]
