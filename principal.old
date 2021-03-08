"""
# Principal.
Módulo principal del programa. Se encarga de gestionar la partida.
"""
from carta import Carta
import repartidor
import jugadores
from random import randint as aleatorio

_tuto = False    # Auxiliar para controlar la disponibilidad del tutorial.
_solitario = False
def principal():
    global _solitario
    print('\nRepartidor.-¡Bienvenido de nuevo!')
    tutorial()  # El tutorial solo se preguntará una vez
    jugadores.asignar_jugadores()
    jugadores.asignar_bots()
    if len(jugadores.jugadores) == 1:
        _solitario = True
    jugar()

def jugar():
    """Gestiona la partida."""
    while jugadores.jugadores != []:
        for jugador in jugadores.jugadores:
            turno(jugador)
            comprobar_fin_jugador(jugador)
        comprobar_fin_juego()

def comprobar_fin_juego():
    if _solitario == True:
        if jugadores.jugadores == []:       # Si no queda ningún jugador con vida
            finalizar()
    else:
        if len(jugadores.jugadores) == 1:   # Si sólo queda un jugador
            print(jugadores.jugadores[0]['nombre'], 'gana esta partida!')
            jugadores.borrar_jugador(jugadores
                                     .jugadores[0])
            finalizar()

def comprobar_fin_jugador(jugador):
    if jugadores.vida(jugador) <= 0:
        print ('Repartidor.- Que triste...', jugadores.nombre(jugador), 'se ha desmayado.')
        print('(Dos matones arrastran al cuerpo de', jugadores.nombre(jugador), 'fuera de la sala.')
        jugadores.borrar_jugador(jugador)
        input('Pulsa una tecla para continuar...')


def turno(jugador):
    """Ejecuta el turno de un jugador. Varia dependiendo de si el jugador es un bot"""
    print('\nRepartidor.- Es el turno de', jugadores.nombre(jugador), '\nPonte cómodo mientras barajo.')
    if jugador['tipo'] == jugadores.BOT:
        seleccion = aleatorio(0, 3)   # El bot ya tiene decidido que carta va a escoger.
        cartas.barajar()
        print(jugadores.nombre(jugador), 'ha seleccionado la carta nº', (seleccion + 1))
        print('\nRepartidor.- Veamos como escapa nuestro compañero...')
        print('(El repartidor voltea tu carta y...)')
        cartas.mostrar()
        repartidor.comprobar(cartas.baraja[seleccion], jugador)  # [...] Y comprueba su elección.
    else:
        cartas.barajar()
        seleccion = repartidor.repartir()   # El jugador selecciona una carta del reparto.
        print(jugadores.nombre(jugador), 'ha seleccionado la carta nº', (seleccion))
        print('\nRepartidor.- Veamos que terrible destino te espera...')
        print('(El repartidor voltea tu carta y...)')
        cartas.mostrar()
        repartidor.comprobar(cartas.baraja[seleccion], jugador)
    print('La vida de', jugadores.nombre(jugador), 'es de:', jugadores.vida(jugador))
    input('Pulsa una tecla para continuar...')

def repetir():
    """Pregunta al jugador si quiere vovler a jugar una nueva partida"""
    correcto = False    # Auxiliar para controlar la ejecución de la sentencia while.
    respuesta = None
    while not correcto:
        try:
            respuesta = input('¿Te gustaría probar suerte de nuevo (S/N)?: ').upper()
            if respuesta == 'S' or respuesta =='Y':
                print('Repartidor.- Muy bien, volvamos a empezar entonces')
                return True
            elif respuesta == 'N':
                print('Repartidor.- De acuerdo. ¡Vuelve cuando quieras!')
                return False
        except ValueError:
            print('Por favor, elige una opción válida.')

def finalizar():
    """El repartidor pregunta al jugador si quiere volver a jugar."""
    print('\nRepartidor.- Bueno, esto ha sido todo por ahora.')
    decision = repetir()
    if decision == True:
        principal()
    else:
        print('(El repartidor se desvanece en la oscuridad.)')

def tutorial():
    """Pregunta al jugador si quiere que se le explique las reglas del juego."""
    global _tuto # Cambiaremos _tuto para omitir el tutorial.
    if _tuto == True:
        return
    else:
        correcto = False
        while not correcto:
            try:
                respuesta = input('¿Quieres que te explique las reglas del juego (S/N)?: ').upper()
                if respuesta == 'S' or respuesta =='Y':
                    repartidor.explicar()
                    correcto = True
                elif respuesta == 'N':
                    correcto = True
            except TypeError:
                print('Por favor, elige una opción válida.')
        _tuto = True

if __name__ == "__main__":
    principal()
