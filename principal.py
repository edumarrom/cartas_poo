from carta import  Naipe
from jugador import Jugador

def principal():
    Naipe.generar_baraja()
    Jugador.asignar_bots(4)
    Naipe.barajar()
    repartir_mesa(3)
    mostrar_mesa()

    print(f'Baraja descubierta:\n{Naipe.mostrar_baraja()}')

    repartir_mesa(3)
    mostrar_mesa()

    print(f'Naipes restantes:\n{Naipe.mostrar_baraja()}')


def repartir_mesa(num_cartas):
    for jugador in Jugador.jugadores():
        jugador.recibir_mano(Naipe.repartir(num_cartas))

def mostrar_mesa():
    for jugador in Jugador.jugadores():
        print(jugador)

if __name__ == "__main__":
    principal()
