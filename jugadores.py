"""
# Jugadores
Aloja a los jugadores en una lista y sus datos en un diccionario.
Tienen esta estructura:
- Jugador {'nombre' : 'jugador1', 'vida' : VIDA_INICIAL, 'tipo' : HUMANO | BOT}
"""
from random import randint as aleatorio

HUMANO = False
BOT = True
VIDA_INICIAL = 4
jugadores = []

nombres = ('Lucía', 'Roberto', 'Belén', 'Alicia',
           'Juan', 'Paloma', 'Natalia', 'Josemi','Andrés', 'Isabel', 'Pablo','Álex',
           'Vicenta', 'Marisa', 'Concha', 'Mauri', 'Fernando',
           'Emilio', 'Mariano', 'Paco'
           )

def crear_jugador(nombre_jugador):
        """Crea un jugador y lo añade a la lista de jugadores."""
        jugadores.append({'nombre' : nombre_jugador, 'vida' : VIDA_INICIAL, 'tipo' : HUMANO})

def crear_bot(nombre_bot):
        """Crea un jugador y lo añade a la lista de jugadores."""
        jugadores.append({'nombre' : nombre_bot, 'vida' : VIDA_INICIAL, 'tipo' : BOT})

def borrar_jugador(jugador):
        """Borra un jugador de la lista de jugadores."""
        jugadores.remove(jugador)

def vida(jugador):
        """Devuelve la vida del jugador pasado como argumento."""
        return jugador['vida']

def nombre(jugador):
        """Devuelve el nombre del jugador pasado como argumento."""
        return jugador['nombre']

def modificar_vida(valor, jugador):
        """Modifica la vida del jugador pasado como argumento.
        - Args:
                - valor (int): Ea cantidad de vida que se quiere sumar o restar.
                - jugador: El jugador al que vamos a modificar su vida.
        """
        jugador['vida'] = jugador['vida'] + (valor)
        """
        [¿Es lógico que el módulo jugadores elimine a los jugadores vencidos?]
        if jugador['vida'] <= 0:
                borrar_jugador(jugador)
        """

def asignar_jugadores():
        """Creador interactivo de jugadores. Solicita nombres."""
        num_jugadores = int(input('¿Cuántas personas quieres añadir?: '))
        for i in range(num_jugadores):
                try:
                        nombre_jugador = str(input('¿Nombre del jugador?: '))
                        crear_jugador(nombre_jugador)
                except ValueError:
                        print('Por favor, elige una opción válida.')

def asignar_bots():
        """Creador interactivo de jugadores. Asigna nombre de forma automática."""
        num_bots = int(input('¿Cuántos bots quieres añadir?: '))
        for i in range(num_bots):
                nombre_bot = nombres[aleatorio(0, (len(nombres) - 1))]
                crear_bot(nombre_bot)

"""
ANTIGUO ASIGNAR_JUGADORES ANTES DE INTRODUCIR ASIGNAR_BOTS
def asignar_jugadores():
        "
        Creador interactivo de jugadores. Solicita nombre y
        "
    num_jugadores = int(input('¿Cuántos van a jugar esta vez?: '))
    for i in range(num_jugadores):
        nombre_jugador = input('¿Nombre del jugador?: ')
        try:
            respuesta = input('¿Es un bot (S/N)?: ').upper()
            if respuesta == 'S' or respuesta =='Y':
                crear_jugador(nombre_jugador, True)
            elif respuesta == 'N':
                crear_jugador(nombre_jugador, False)
        except ValueError:
                print('Por favor, elige una opción válida.')
"""
