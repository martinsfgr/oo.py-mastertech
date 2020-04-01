from random import randint

class Cliente():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Conta():
    def __init__(self, cliente):
        self.titular = cliente
        self.numero_conta = self.gerar_numero()
        self.saldo = 0

    def gerar_numero(self):
        self.numero_aleatorio = f'{randint(1000, 9999)}-{randint(1, 9)}'
        return self.numero_aleatorio

    def consultar_saldo(self):
        return self.saldo
    
    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
    
    def sacar(self, valor_saque):
        self.saldo -= valor_saque
        