from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
   [sg.Text('Usuário')],
   [sg.Input(key='usuario', size=(25,1))],
   [sg.Text('Senha')],
   [sg.Input(key='senha', password_char=('*'),size=(25,1))],
   [sg.Checkbox('Salvar o Login')],
   [sg.Button('Entrar')]
]
#Janela
janela = sg.Window('Login', layout)
# Ler Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        usuario_padrao = 'adm'
        senha_padrao = '123'
        usuario = valores['usuario']
        senha = valores['senha']
        if valores['usuario']=='adm'and valores['senha']=='123':
            print('Bem Vindo!!!')

