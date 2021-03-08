"""
# Repartidor.
Se encarga de repartir y comprobar las cartas.
"""
import cartas
import jugadores
from random import shuffle as mezclar

def comprobar(carta, jugador):
    # Comprueba y anuncia la carta elegida por el jugador.
    if carta == cartas.GE:
        jugadores.modificar_vida(2, jugador)
        print('Repartidor.- ¡La fortuna te sonríe, gran éxito!.')
    elif carta == cartas.E:
        jugadores.modificar_vida(1, jugador)
        print('Repartidor.- No está mal ¡Es un éxito!.')
    elif carta == cartas.F:
        jugadores.modificar_vida(- 1, jugador)
        print('Repartidor.- Mas suerte la proxima vez, es un fracaso.')
    elif carta == cartas.GF:
        jugadores.modificar_vida(- 2, jugador)
        print('Repartidor.- La desgracia se cierne sobre tí, es un gran fracaso.')

def repartir():
    """Reparte las cartas al jugador y le de la opción de elegir una de ellas."""
    correcto = False    # Auxiliar para controlar la ejecución de la sentencia while
    seleccion = None
    print()
    print ('[XX] [XX] [XX] [XX]')
    print()
    while not correcto:
        try:
            seleccion = int(input('Elige una carta([1 - 4]): ')) - 1
            if seleccion < 4:
                correcto = True
            else:
                print('Repartidor.- Por favor, elige una opción válida ([1 - 4]).')
        except ValueError:
            print('Repartidor.- Por favor, elige una opción válida ([1 - 4]).')
    return seleccion

def explicar():
    """Explica al jugador las reglas del juego."""
    correcto = False    # Auxiliar para controlar la ejecución de la sentencia while.
    respuesta = ''
    print('\nRepartidor.- Bien, presta atención, seré breve:')
    print('\nVoy a barajar 4 cartas y tu tendrás que seleccionar una de ellas.')
    print('Las cartas pueden presentar los siguientes valores:')
    print('\n[Gran Éxito] | [Éxito] | [Fracaso] | [Gran Fracaso]')
    print('\nTendrás que elegir una al azar, y así descubriremos tu destino')
    while not correcto:
        try:
            respuesta = input('¿Quieres que te lo repita (S/N)?: ').upper()
            if respuesta == 'S' or respuesta =='Y':
                explicar()
                correcto = True
            elif respuesta == 'N':
                correcto = True
        except ValueError:
            print('Por favor, elige una opción válida.')
