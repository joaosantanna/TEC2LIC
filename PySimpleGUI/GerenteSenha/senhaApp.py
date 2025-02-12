import PySimpleGUI as sg
from funcionalidades import gerar_senha, salvar_conta

sg.theme("LightGrey1")

contas = []

layout = [
    [sg.Text("Gerenciador de senhas", font=("Helvetica", 25))],
    [sg.Text("Conta:", size=(8, 1)), sg.InputText(key="-CONTA-", size=(20, 1))],
    [sg.Text("Login:", size=(8, 1)), sg.InputText(key="-LOGIN-", size=(20, 1))],
    [
        sg.Text("Senha:", size=(8, 1)),
        sg.InputText(key="-SENHA-", password_char="*", size=(20, 1)),
        sg.Checkbox("Ver", key="-MOSTRAR-", enable_events=True),
    ],
    [
        sg.Text("Campos"),
        sg.Button("Gerar senha"),
        sg.Spin(
            [i for i in range(6, 31)], initial_value=6, key="-TAMANHO-", size=(2, 1)
        ),
    ],
    [
        sg.Checkbox("Maiusculas", key="-MAIUSCULAS-", default=True),
        sg.Checkbox("Minusculas", key="-MINUSCULAS-", default=True),
        sg.Checkbox("Digitos", key="-DIGITOS-"),
        sg.Checkbox("Simbolos", key="-SIMBOLOS-"),
    ],
    [sg.Button("Salvar", size=(8, 1)), sg.Button("Sair", size=(8, 1))],
]

janela = sg.Window("Gerenciador de senhas", layout, font=("Helvetica", 14))

while True:
    evento, valores = janela.read()

    if evento in (sg.WIN_CLOSED, "Sair"):
        break
    if evento == "Gerar senha":
        tamanho = valores["-TAMANHO-"]
        maiusculas = valores["-MAIUSCULAS-"]
        minusculas = valores["-MINUSCULAS-"]
        digitos = valores["-DIGITOS-"]
        simbolos = valores["-SIMBOLOS-"]
        senha = gerar_senha(tamanho, maiusculas, minusculas, digitos, simbolos)
        janela["-SENHA-"].update(senha)

    if evento == "-MOSTRAR-":
        if valores["-MOSTRAR-"]:
            janela["-SENHA-"].update(password_char="")
        else:
            janela["-SENHA-"].update(password_char="*")

    if evento == "Salvar":
        conta = valores["-CONTA-"]
        login = valores["-LOGIN-"]
        senha = valores["-SENHA-"]
        contas.append({"conta": conta, "login": login, "senha": senha})
        salvar_conta(contas)
        sg.popup("Conta salva com sucesso!")
janela.close()
