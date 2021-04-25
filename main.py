from PySimpleGUI import PySimpleGUI as sg
import random


# criação do layout
def janela_dificuldade():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Bem-vind@ ao super jogo \"Adivinhe o que estou pensando!\"')],
        [sg.Text('Selecione o seu nível de dificuldade:')],
        [sg.Radio('Fácil', "valor", default=True, enable_events=True, key='n1'), sg.Radio('Médio', "valor", enable_events=True, key='n2'), sg.Radio('Difícil', "valor", enable_events=True, key='n3'), sg.Radio('LENDÁRIO', "valor", enable_events=True, key='n4')],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Seleção de dificuldade', layout=layout, finalize=True)


def janela_principal():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Eu escolhi um número ao acaso. Tente descobri-lo no menor número de tentativas possível!')],
        [sg.Text('Digite um número entre 1 e %d' % maxn)],
        [sg.Input(key='palpite', size=(5, 1))],
        [sg.Button('Verificar')]
    ]
    return sg.Window('Janela principal', layout=layout, finalize=True)


# criação da janela
janela0, janela1 = janela_dificuldade(), None
# eventos
while True:             # laço principal
    janela, eventos, valor = sg.read_all_windows()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Continuar' and valor['n1'] is True:
        maxn = 20
        n = random.randint(1, maxn)
        janela0.hide()
        janela1 = janela_principal()
    elif eventos == 'Continuar' and valor['n2'] is True:
        maxn = 50
        n = random.randint(1, maxn)
        janela0.hide()
        janela1 = janela_principal()
    elif eventos == 'Continuar' and valor['n3'] is True:
        maxn = 100
        n = random.randint(1, maxn)
        janela0.hide()
        janela1 = janela_principal()
    elif eventos == 'Continuar' and valor['n4'] is True:
        maxn = 1000
        n = random.randint(1, maxn)
        janela0.hide()
        janela1 = janela_principal()
    if eventos == 'Verificar' and int(valor['palpite']) == n:
        sg.popup('Parabéns, você adivinhou!')
        break
    elif eventos == 'Verificar' and int(valor['palpite']) < n:
        sg.popup('Seu palpite está ABAIXO do número que eu pensei! Tente novamente.')
    elif eventos == 'Verificar' and int(valor['palpite']) > n:
        sg.popup('Seu palpite está ACIMA do número que eu pensei! Tente novamente.')
