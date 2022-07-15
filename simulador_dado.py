# Simulador de dado
# Simular o uso do dado, gerando um valor de 1 até 6
from logging import exception
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # layout
        self.layout = [
            [sg.Text('Jogar o Dado?')],
            [sg.Button('sim'),sg.Button('não')]
        ]

    def Iniciar(self): 
        # criar janela
        self.janela = sg.Window('Simulador de dado',layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.read()
        # fazer algo com os valores
        try:
                if self.eventos == 'sim' or self.eventos == 's':
                    self.GerarValorDoDado()
                elif self.eventos == 'não' or self.eventos == 'n':
                    print('Muito Obrigado por Participar!')    
                else:
                    print('Por favor digite sim ou não')
        except:
                print('Erro ao receber sua resposta')                

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()        