from classes import Cliente, Conta

class CaixaEletronico():
    def __init__(self):
        nome_cliente = input('Digite o seu nome: ')
        cpf_cliente = input('Digite seu CPF (Apenas números): ')
        cliente = Cliente(nome_cliente, cpf_cliente)
        self.conta = Conta(cliente)

        print(f'Olá, {self.conta.titular.nome}, sua conta é {self.conta.numero_conta}')

    def exibir_menu(self):
        print(f'1- Consultar saldo\n2- Depositar\n3- Sacar')
        escolha = int(input('Escolha uma opção: '))

        if escolha == 1:
            print('Entrei aqui')
            valor_saldo = str(self.conta.consultar_saldo())
            print(f'Seu saldo é R$ {valor_saldo}')

        if escolha == 2:
            valor_deposito = float(input('Digite o valor que deseja depositar: '))
            self.conta.depositar(valor_deposito)
            print(f'{valor_deposito} depositado com sucesso.')
            
        
        if escolha == 3:
            valor_saque = float(input('Digite o valor que deseja sacar: '))
            if self.conta.saldo < valor_saque:
                print(f'Saldo insuficiente, pois você possui {self.conta.saldo}, e deseja sacar {valor_saque}')
            elif valor_saque > 0 and self.conta.saldo > valor_saque:
                self.conta.sacar(valor_saque)
                print(f'O saque de {valor_saque} foi feito com sucesso')
