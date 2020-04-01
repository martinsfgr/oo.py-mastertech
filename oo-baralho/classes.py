from random import randint

ranks = (
    ('Ás', 1),
    ('Dois', 2),
    ('Três', 3),
    ('Quatro', 4),
    ('Cinco', 5),
    ('Seis', 6),
    ('Sete', 7),
    ('Oito', 8),
    ('Nove', 9),
    ('Dez', 10),
    ('Valete', 10),
    ('Dama', 10),
    ('Rei', 10),   
)

naipes = ('Paus', 'Copas', 'Espadas', 'Ouros')

class Carta():
    def __init__(self, naipe, rank, valor):
        self.naipe = naipe
        self.rank = rank
        self.valor = valor

    def __str__(self):
        return f'{self.rank} de {self.naipe} [{self.valor}]'

class Baralho():
    def __init__(self):
        self.cartas = []

        for naipe in naipes:
            for rank in ranks:
                carta = Carta(naipe, rank[0], rank[1])
                self.adicionar_carta(carta)

    def __str__(self):
        string = ''

        for carta in self.cartas:
            string += str(carta)
            string += ', '
        return string

    def adicionar_carta(self, carta):
        self.cartas.append(carta)

    def remover_carta(self):
        return self.cartas.pop()

    def sortear_carta(self):
        numero_sorteado = randint(0, len(self.cartas)-1)
        return self.cartas.pop(numero_sorteado)

class Jogo21():
    def __init__(self):
        self.baralho = Baralho()
        self.pontuacao = 0
        
    def executar_primeira_rodada(self):
        carta_um = self.baralho.sortear_carta()
        carta_dois = self.baralho.sortear_carta()
        self.pontuacao = carta_um.valor + carta_dois.valor

        return [carta_um, carta_dois]
    
    def executar_rodada(self):
        carta = self.baralho.sortear_carta()
        self.pontuacao += carta.valor

        return carta

    def apurar_pontos(self):
        return self.pontuacao >= 21