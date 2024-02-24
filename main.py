from jogo_func import *

# Inicia o Jogo
jogo = Jogo()

# Cria a lista de opções
possibilidades = ['Pedra', 'Papel', 'Tesoura']

# Loop do jogo
while True:
    loop = True
    jogo.tela_titulo()
    resposta_pes = jogo.perguntar_escolha()
    resposta_pc = jogo.escolher_pc()
    print('~'*30)
    print(f'Escolha o Humano: {possibilidades[resposta_pes]}\nEscolha da Máquina {possibilidades[resposta_pc]}')
    print('~'*30)
    resultado = jogo.tela_resultado(escolha_pc=resposta_pc, escolha_pes=resposta_pes)
    while loop:
        loop, continuar = jogo.continuar()
    if continuar:
        continue
    else:
        break