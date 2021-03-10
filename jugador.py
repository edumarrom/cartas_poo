from random import randint as aleatorio
from carta import Naipe

VIDA_INICIAL = 0

class Jugador:
    """
    Clase Jugador
    ---
    La clase Jugador representa a un jugador y almacena información \
    sobre éste, compuesta principalmente por su nombre, su salud y \
    su mano de cartas. Los jugadores pueden ser bots controlados por \
    el programa.
    """
    __ultimo = 0
    __jugadores = []

    def __init__(self, nombre, vida, bot):
        Jugador.__ultimo += 1
        if Jugador.comprobar_nombre(nombre) is True:
            self.__numero = self.__ultimo
            self.__nombre = nombre
            self.__vida = vida
            self.__bot = bot
            Jugador.__jugadores.append(self)
            self.__mano = []
        else:
            print('Lo sentimos, pero ya existe un jugador con el nombre "'+ nombre +'".')

    def __repr__(self):
        return f"Jugador('{self.__nombre}', '{self.__vida}, {self.__bot}'')"

    def __str__(self):
        return f'{self.nombre()} | Salud: {self.vida()} | Mano({len(self.mano())}):\n {Naipe.mostrar_cartas(self.mano())}'

    @staticmethod
    def get_jugador(seleccion):
        """
        Devuelve una jugador existente en la lista a partir de su número.\n
        Parámetros:
            - seleccion: int -> El n-ésima jugador de la lista.
        """
        return Jugador.jugadores()[seleccion]

    def numero(self):
        return self.__numero

    def nombre(self):
        return self.__nombre

    def vida(self):
        return self.__vida

    def bot(self):
        return self.__bot

    def mano(self):
        return self.__mano

    def set_mano(self, mano):
        self.__mano = mano

    def recibir_mano(self, mano):
        self.__mano += mano

    def devolver_mano(self):
        aux = Naipe.baraja()
        aux += self.mano()
        self.__mano = []
        Naipe.__baraja = aux

    def borrar_jugador(jugador):
        """Borra un jugador de la lista de jugadores."""
        Jugador.jugadores().remove(jugador)

    @staticmethod
    def jugadores():
        return Jugador.__jugadores

    @staticmethod
    def nombre_aleatorio():
        nombres = (
            'Lucía', 'Roberto', 'Belén', 'Alicia', 'Juan', 'Paloma', \
            'Natalia', 'Josemi','Andrés', 'Isabel', 'Pablo','Álex', \
            'Vicenta', 'Marisa', 'Concha', 'Mauri', 'Fernando', 'Emilio', \
            'Mariano', 'Paco'
            )
        return nombres[aleatorio(0, (len(nombres) - 1))]

    @staticmethod
    def comprobar_nombre(nombre):
        resultado = True
        for jugador in Jugador.jugadores():
            if nombre == jugador.nombre():
                resultado = False
        return resultado

    @staticmethod
    def asignar_humanos(num_jugadores):
        """
        Creador interactivo de humanos. Solicita por entrada el \
            nombre del jugador
        """
        for i in range(num_jugadores):
            try:
                nombre_jugador = str(input('¿Nombre del jugador?: '))
            except ValueError:
                print('Por favor, elige una opción válida.')
            Humano(nombre_jugador)

    @staticmethod
    def asignar_bots(num_bots):
        """
        Creador interactivo de bots. Asigna nombres de forma automática
        """
        while len(Jugador.jugadores()) < (num_bots+1)*2:
            nombre = Jugador.nombre_aleatorio()
            if Jugador.comprobar_nombre(nombre) is True:
                Bot(nombre)
                num_bots -= 1


class Humano(Jugador):
    """
    Clase Humano
    ---
    La clase Humano representa a un jugador humano de la partida. Se \
        espera que estos jugadores tomen decisiones propias.
    """
    def __init__(self, nombre):
        super().__init__(nombre, VIDA_INICIAL, False)

    def __str__(self):
        return f'Humano: {super().__str__()}'

class Bot(Jugador):
    """
    Clase Bot
    ---
    La clase Bot representa a un jugador de la partida, controlado \
        por la máquina.
    """
    def __init__(self, nombre):
        super().__init__(nombre, VIDA_INICIAL, True)

    def __str__(self):
        return f'BOT: {super().__str__()}'
