from interface import CaixaEletronico

caixa_eletronico = CaixaEletronico()

resposta = ''

while resposta != "SAIR":
    resposta = input(f'E - Executar ação no Caixa Eletrônico\nS- Sair do Caixa Eletrônico')

    if resposta == "E":
        caixa_eletronico.exibir_menu()

    else:
        print('Resposta inválida')
