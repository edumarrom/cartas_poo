from carta import  Naipe
from jugador import Jugador

_tuto = False    # Auxiliar para controlar la disponibilidad del tutorial.
_solitario = False
_inicio = False
def comenzar():
    global _solitario
    global _inicio
    print('\nRepartidor.-¡Bienvenido de nuevo!')
    # tutorial()  # El tutorial solo se preguntará una vez
    if _inicio is False:
        Naipe.generar_baraja()
        _inicio = True
    Naipe.barajar()
    num_humanos = int(input('¿Cuántas personas quieres añadir?: '))
    Jugador.asignar_humanos(num_humanos)
    # num_bots = int(input('¿Cuántos bots quieres añadir?: '))
    # Jugador.asignar_bots(num_bots)

    if len(Jugador.jugadores()) == 1:
        _solitario = True
    jugar()

def jugar():
    """Gestiona la partida."""
    for jugador in Jugador.jugadores():
        turno(jugador)
        comprobar_fin_jugador(jugador)
    comprobar_fin_juego()

def turno(jugador):
    """Ejecuta el turno de un jugador. Varia dependiendo de si el jugador es un bot"""
    print('\nRepartidor.- Es el turno de', jugador.nombre(), '\nPonte cómodo mientras barajo.')
    # if jugador.bot() is True: Por el momento no hay bots
    jugador.recibir_mano(Naipe.repartir(1))
    correcto = False
    while not correcto:
        print(f'Total: {Naipe.sm_valores(jugador.mano())} | Mano: \n{Naipe.mostrar_cartas(jugador.mano())}')
        try:
            respuesta = input('¿Quieres otra carta (S/N)?: ').upper()
            if respuesta == 'S' or respuesta =='Y':
                jugador.recibir_mano(Naipe.repartir(1))
            elif respuesta == 'N':
                correcto = True
        except TypeError:
            print('Por favor, elige una opción válida.')
    # input('Pulsa una tecla para continuar...')

def comprobar_fin_jugador(jugador):
    if Naipe.sm_valores(jugador.mano()) > 7.5:
        print (f'Repartidor.- Que triste... {jugador.nombre()} se ha pasado de las siete y media.')
        jugador.devolver_mano()
        Jugador.borrar_jugador(jugador)
        input('Pulsa una tecla para continuar...')

def comprobar_fin_juego():
    if Jugador.jugadores() == []:       # Si no queda ningún jugador con vida
            finalizar()
    ganador = Jugador.get_jugador(0)
    for jugador in Jugador.jugadores():
        if Naipe.sm_valores(ganador.mano()) < Naipe.sm_valores(jugador.mano()):
            ganador = jugador
    print(f'¡{ganador.nombre()} gana esta partida!')
    finalizar()

def recoger_mesa():
    for jugador in Jugador.jugadores():
        jugador.devolver_mano()

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
    recoger_mesa()
    Jugador.limpiar_jugadores()
    decision = repetir()
    if decision == True:
        comenzar()
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
    comenzar()
