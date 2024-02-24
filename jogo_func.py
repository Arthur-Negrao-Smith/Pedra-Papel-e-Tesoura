from random import randint
from time import sleep

class Jogo:
    """O jogo deve ser posto num laço while True para funcionar como previsto"""
    def __init__(self) -> None:
        self.escolha_pes = int
        self.escolha_pc = int

    def tela_titulo(self):
        """mprime uma tela de título"""
        titulo = 'Pedra, Papel e tesoura'
        print(f"{titulo:-^50}")

    def escolher_pc(self) -> int:
        """Serve para escolher um número para o sistema"""
        self.escolha_pc = randint(0, 2)
        return self.escolha_pc
    
    def tela_resultado(self, escolha_pes, escolha_pc):
        if escolha_pes == 0 and escolha_pc == 2 or escolha_pes == 1 and escolha_pc == 0 or escolha_pes == 2 and escolha_pc == 1:
            sleep(0.5)
            print('PARABÉNS! \nVOCÊ GANHOU... Pura sorte...')
        elif escolha_pes == escolha_pc:
            sleep(0.5)
            print('DEU EMPATE! Maldito humano...')
        else:
            sleep(0.5)
            print('Não foi dessa vez HUMANO! HUAHUAHUA')
        
    def continuar(self):
        """Pergunta se o jogo deve continuar e trata os erros"""
        try:
            voltar = input('Deseja continuar? [s/n] ').strip()
            continua = False
            if voltar in '':
                print('Valor inválido')
                continua = True
                return True, continua
            elif voltar in 'snSN':
                if voltar in 'Ss':
                    print('CARREGANDO...')
                    continua = True
                    sleep(0.5)
                    return False, continua
                else:
                    print('Fechando jogo...')
                    continua = False
                    sleep(0.5)
                    return False, continua
            else:
                continua = True 
                return True, continua
        except:
            print('Valor inválido')
            return True, continua

    def perguntar_escolha(self):
        """Serve para perguntar Qual a opção do player"""
        print(f'Pedra[ 0 ] \nPapel [ 1 ] \nTesoura[ 2 ] ')
        while True:
            try:
                self.escolha_pes = int(input('Sua escolha: '))
                if self.escolha_pes not in [0, 1, 2]:
                    print('valor inválido')
                else:
                    break
            except:
                print('Valor inválido')
        return self.escolha_pes

