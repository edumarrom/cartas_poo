from random import shuffle as mezclar

class Carta:
    """
    Clase Carta
    ---
    La clase Carta representa y almacena las cartas en una baraja.
    La carta está compuesta por:
        - corta: str -> Descripción corta de la carta (ej: 'C10')
        - larga: str -> Descripción larga de la carta (ej: 'Rey de copas')

    Ea la baraja, las cartas se identifican por:
        - int numero; Numero que define en que posición se encuentra la carta
        dentro de la baraja.
        - Su valor, compuesto por una carta.

    """
    __baraja = {}
    __ultima = 0

    def __init__(self, corta, larga):
        """Constructor de la clase Carta"""
        Carta.__ultima += 1
        self.__numero = Carta.__ultima
        self.__corta = corta
        self.__larga = larga
        Carta.__baraja[self.__numero] = self

    def __repr__(self):
        return f"Carta('{self.corta()}', '{self.larga()}')"

    @staticmethod
    def get_carta(seleccion):
        """
        Devuelve una carta existente en la baraja a partir de su número.\n
        Parámetros:
            - seleccion: int -> La n-ésima carta de la baraja.
        """
        return Carta.baraja().get(seleccion)

    def numero(self):
        """Devuelve el numero de la carta."""
        return self.__numero

    def corta(self):
        """Devuelve una descripción (o denominación) de la carta."""
        return self.__corta

    def larga(self):
        """Devuelve una descripción larga de la carta."""
        return self.__larga

    @staticmethod
    def baraja():
        """Devuelve la baraja."""
        return Carta.__baraja

    @staticmethod
    def mostrar_cartas(cartas):
        """Devuelve una descripción completas de una lista de cartas recibida."""
        resultado = ''
        for carta in cartas:
            resultado += (f'{carta.describir()}, ')
        return resultado

    @staticmethod
    def mostrar_baraja():
        """Devuelve una descripción completas de todas las cartas de la baraja."""
        resultado = ''
        for carta in Carta.baraja().values():
            resultado += (f'{carta.describir()}, ')
        return resultado

    @staticmethod
    def barajar():
        """Mezcla las cartas de la baraja de forma aleatoria."""
        temp = list(Carta.baraja().values())
        mezclar(temp)
        Carta.__baraja = dict(zip(Carta.baraja(), temp))

    def describir(self):
        """
        Devuelve una descripción completa de una carta de la baraja.\n
        Parámetros:
            - seleccion: int -> La n-ésima carta de la baraja.
        """
        return f'[{self.corta()}] - {self.larga()}'


class Naipe(Carta):
    """
    Clase Naipe
    ---
    La clase Naipe representa cartas de naipes de la baraja española,
    las cuáles se identifican por su palo y su valor.\n
    La descripción corta de un naipe tiene esta composición:
        - El primer caracter del palo : 'Bastos'[0] -> 'B'
        - El literal del valor : 7 -> '7'
        Ejemplo: 'Rey de Bastos' ->'B10'\n
    La descripción larga se trata de un literal en lenguaje natural
    que describe a la carta:
        Ejemplo: Naipe('Copas', 8) -> 'Sota de Copas'.
    """

    def __init__(self, palo, valor):
        super().__init__(Naipe.generar_corta(palo, valor) \
            , Naipe.generar_larga(palo, valor))
        self.__palo = palo
        self.__valor = valor

    def __repr__(self):
        return f"Naipe('{self.palo()}', '{self.valor()}')"

    @staticmethod
    def generar_baraja():
        """Genera una baraja de naipes española de 40 cartas."""
        palos = ['Oros', 'Copas', 'Espadas', 'Bastos']
        valores = list(range(1, 11))
        for palo in palos:
            for valor in valores:
                Naipe(palo, valor)

    @staticmethod
    def generar_corta(palo, valor):
        """Genera una decripción corta de un naipe, a partir de su
        palo y valor."""
        palo = palo[0]
        valor = str(valor)
        return palo + valor

    @staticmethod
    def generar_larga(palo, valor):
        """Genera una decripción larga de un naipe, a partir de su
        palo y valor."""
        literales = ['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis'\
            , 'Siete','Sota', 'Caballero', 'Rey']
        return f'{literales[valor-1]} de {palo}'

    '''
    @staticmethod
    def mostrar_naipes():
        """Descubre todas las naipes de de la baraja, devolviendo su
        descripción corta y larga."""
        resultado = ''
        for naipe in Naipe.baraja().values():
            resultado += (f'[{naipe.corta()}] - {naipe.larga()}, ')
        return resultado
    '''

    @staticmethod
    def repartir(cantidad):
        """Reparte una cantidad de cartas de la baraja, retirandolas de
        la misma y devolviéndolas."""
        aux = []
        while cantidad > 0:
            for numero in Naipe.baraja():
                aux.append(Naipe.get_carta(numero))
                del Naipe.baraja()[numero]
                break
            cantidad -= 1
        return aux

    def palo(self):
        """"Devuelve el palo de un naipe."""
        return self.__palo

    def valor(self):
        """Devuelve el valor de un naipe."""
        return self.__valor

    def comparar_naipes(naipe1, naipe2):
        """Compara dos cartas y devuelve la de valor superior."""
        if naipe1.valor() > naipe2.valor():
            return naipe1
        else: return naipe2

if __name__ == "__main__":
    print('Esto es una pequeña demostración de que cómo funciona la clase Carta y, en especial, la subclase Naipe.\n')
    Naipe.generar_baraja()
    print(f'Primero vamos a desempolvar la baraja, y vamos a poner todas nuestras cartas boca arriba:\n{Naipe.mostrar_baraja()}\n')

    print(f'Impecable y ordenada. Un detalle interesante es que puedo obtener en todo momento una carta a partir de su posición. Por ejemplo, la carta en la posición 28 es: {Naipe.get_carta(28)}\n')
    print(f'O mejor aún, podemos obtener una descripción literal de que carta se trata, por ejemplo, de la carta 17: {Naipe.get_carta(17).describir()}\n')

    print('También podemos hacer algo muy interesante. Comparar dos cartas. Comparamos sus valores y nos devuelve la de mayor valor.')
    print(f'Vamos por ejemplo a comparar las dos cartas que hemos obervado antes, la sota de espadas y el 7 de copas: {Naipe.comparar_naipes(Naipe.get_carta(28), Naipe.get_carta(17))}')
    print('Como era de esperar, nos devuelve la sota de Espadas, por tener un valor mayor. (8 > 7)') # Más adelante incluiré el factor de la "vira", que hara que un palo tenga mayor valor que el resto de naipes

    print('Ahora vamos a barajar las cartas cuidadosamente...')
    Naipe.barajar()
    print(f'Y tras barajar, la carta de la posición 28 ya no es la sota de espadas, ahora es: {Naipe.get_carta(28).describir()}\n')
    print(f'Volvamos a ver la baraja para confirmar que está completamente mezlcada:\n{Naipe.mostrar_baraja()}\n')

    """
    Repartiremos las 3 cartas primeras cartas que se encuentren en la cima de la baraja y por consiguiente son retiradas de la baraja. Por el momento
    estas cartas no van a ningún sitio, pero pretendo que la clase Jugador las reciba y guarde con el nombe de "mano".
    """

    print(f'Vamos a repartir las tres primeras cartas que hay arriba de la baraja:\n{Naipe.repartir(3)}\n')
    print(f'Ahora si volvemos a ver una vez más la baraja, podremos ver que esas 3 cartas ya no se encuentran:\n{Naipe.mostrar_baraja()}\n')
'''
class Yugi(Carta):
    def __init__(self, corta, larga, ataque, defensa):
        super().__init__(corta, larga)
        self.__ataque = ataque
        self.__defensa = defensa

    def __repr__(self):
        return f'Tugi({self.__corta}, {self.__larga}, {self.__ataque}, {self.__defensa})'

    def ataque(self):
        """Devuelve el ataque de la carta."""
        return self.__ataque

    def defensa(self):
        """Devuelve el defensa de la carta."""
        return self.__defensa

    def calcular_danyo(carta1, carta2):
        diferencia = carta2.defensa() - carta1.ataque()

Código para pruebas:
carta1 = Carta('GE', 'Gran exito')
carta2 = Carta('E', 'Exito')
carta3 = Carta('F', 'Fracaso')
carta4 = Carta('GF', 'Gran Fracaso')

print(Carta.mostrar_cartas())

--BASURA--
if self.corta(0) = 'O':
            return 'Oros'
        if self.corta(0) = 'C':
            return 'Copas'
        if self.corta(0) = 'E':
            return 'Espadas'
        if self.corta(0) = 'B':
            return 'Bastos'
'''
