from classes import Jogo21

class Interface():
    def __init__(self):
        self.jogo = Jogo21()

        sorteio = self.jogo.executar_primeira_rodada()
        print(sorteio[0])
        print(sorteio[1])
    
    def jogar_rodada(self):
        sorteio = self.jogo.executar_rodada()
        
        print(f'A carta da rodada é {sorteio}')
        print(f'Sua pontuação é {self.jogo.pontuacao}')

    def encerrar_jogo(self):
        print('Jogo encerrado. Sua pontuação foi ' + str(self.jogo.pontuacao))
        if self.jogo.pontuacao == 21:
            print('=)')

    def continuar_jogo(self):
        if self.jogo.apurar_pontos():
            self.encerrar_jogo()
            return False

        escolha_jogador = input('Deseja continuar? Digite S para comprar mais uma carta, ou N para parar ')

        if escolha_jogador == 'S':
            return True

        elif escolha_jogador == 'N':
            self.encerrar_jogo()
            return False
