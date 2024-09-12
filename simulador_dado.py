import random
from time import sleep


class SimuladorDados:
    def __init__(self):
        self.__dados = [4, 6, 8, 10, 12, 20, 100]

    def lanca_dado(self, tipo: int, quantidade_de_dados: int = 1):
        valor_max = tipo
        lancamentos = quantidade_de_dados
        resultados = []
        retorno = None
        if lancamentos > 1:
            for dado in range(lancamentos):
                resultado = random.randint(1, valor_max)
                print(f'O dado {dado+1} deu: {resultado}')
                resultados.append(resultado)
                retorno = resultados
        else:
            resultado = random.randint(1, valor_max)
            print(f'Resultado: {resultado}')
            retorno = resultado

        return retorno

    def soma_resultado(self, lista):
        soma = 0
        for i in lista:
            soma = soma + int(i)
        return soma

    def execute(self):
        print('Olá, qual é o seu nome?')
        sleep(1)
        player = input('Seu nome: ')
        sleep(2)
        print(f'Prazer em te conhecer { player }')
        sleep(1)
        lancar = True
        while lancar == True:
            print('Você quer lançar um dado? ')
            sleep(2)
            print('Sim (1)')
            print('Não (2)')
            try:
                resposta = int(input('Sua resposta: '))
                if resposta == 1:
                    # Seleção de dado
                    print('Vamos Jogar')
                    sleep(1)
                    print('Que tipo de dado você quer lançar?')
                    sleep(2)
                    contador = 0
                    for dado in self.__dados:
                        print(f'D{dado} ({contador})')
                        contador += 1
                        sleep(1)
                    try:
                        tipo = int(input('Sua resposta: '))
                    except:
                        print('Resposta invalida, tente de novo')
                    sleep(2)
                    print(f'Você vai lançar o D{ self.__dados[tipo] }')
                    sleep(1)
                    # Seleção de quantidade
                    print('Quantos dados você quer jogar?')
                    sleep(1)
                    try:
                        qtd = int(
                            input('Sua resposta(deve ser um numero inteiro): '))
                    except:
                        print('Resposta invalida, tente de novo')
                    resultado = self.lanca_dado(self.__dados[tipo], qtd)
                    if type(resultado) == list:
                        resultado = self.soma_resultado(resultado)
                    print(
                        f'Você lançou {qtd} D{self.__dados[tipo]} e obteve {resultado} como resultado')
                    sleep(10)

                elif resposta == 2:
                    lancar = False
                    print('ok')

            except:
                print('Resposta invalida, tente de novo')


if __name__ == '__main__':
    SimuladorDados().execute()