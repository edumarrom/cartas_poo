from carta import  Naipe
from jugador import Jugador

def principal():
    Naipe.generar_baraja()
    Jugador.asignar_humanos(1)
    Naipe.barajar()
    siete_media()

def siete_media():
    removidos = [] # jugadores que se han pasado.
    Naipe.barajar()
    correcto = False
    for jugador in Jugador.jugadores():
        jugador.recibir_mano(Naipe.repartir(1))
        while not correcto:
            print(f'Total: {Naipe.sm_valores(jugador.mano())} | Mano: \n{Naipe.mostrar_cartas(jugador.mano())}')
            if Naipe.sm_valores(jugador.mano()) > 7.5:
                correcto = True
                print(f'¡Perdiste! {jugador.nombre()}')
                removidos.append(jugador)
                Jugador.borrar_jugador(jugador)
                continue
            try:
                respuesta = input('¿Quieres otra carta (S/N)?: ').upper()
                if respuesta == 'S' or respuesta =='Y':
                    jugador.recibir_mano(Naipe.repartir(1))
                elif respuesta == 'N':
                    correcto = True
            except TypeError:
                print('Por favor, elige una opción válida.')
    finalizar()

"""
def comprobar_fin_jugador(jugador):
    if Naipe.sm_valores(jugador.mano()) > 7.5:
        print ('Repartidor.- Que triste...', jugador.nombre(), 'se ha desmayado.')
        jugadores.borrar_jugador(jugador)
        input('Pulsa una tecla para continuar...')
        # DESPUES
    if Naipe.sm_valores(jugador.mano()) > 7.5:
        print(f'¡Perdiste! {jugador.nombre()}')
        removidos.append(jugador)
        Jugador.borrar_jugador(jugador)
"""

def repetir():
    """Pregunta si se quiere vovler a jugar otra partida."""
    correcto = False
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
    """Pregunta al jugador si quiere volver a jugar."""
    recoger_mesa()
    print('\nRepartidor.- Bueno, esto ha sido todo por ahora.')
    decision = repetir()
    if decision == True:
        siete_media()
    else:
        print('(El repartidor se desvanece en la oscuridad.)')

def repartir_mesa(num_cartas):
    for jugador in Jugador.jugadores():
        jugador.recibir_mano(Naipe.repartir(num_cartas))

def mostrar_mesa():
    for jugador in Jugador.jugadores():
        print(jugador)

def recoger_mesa():
    for jugador in Jugador.jugadores():
        jugador.devolver_mano()

if __name__ == "__main__":
    principal()

"""
Naipe.generar_baraja()
Jugador.asignar_bots(4)
Naipe.mostrar_baraja()
Naipe.barajar()
Naipe.mostrar_baraja()
repartir_mesa(3)
mostrar_mesa()

print(f'Naipes restantes:\n{Naipe.mostrar_baraja()}')

recoger_mesa()

mostrar_mesa()

print(f'Baraja devuelta:\n{Naipe.mostrar_baraja()}')
"""
