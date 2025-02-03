import PySimpleGUI as sg
from math import sqrt

sg.theme("LightGrey1")  # Add a touch of color

layout = [
    [sg.Text("Digite o valor para calcular a raiz Quadrada")],
    [sg.Text("Valor", size=(15, 1)), sg.InputText()],
    [sg.Text("Resultado", size=(15, 1)), sg.InputText(key="Resultado")],
    [sg.Button("Calcular", size=(10, 1)), sg.Button("Sair", size=(10, 1))],
]

janela = sg.Window("Calculadora de raiz quadrada", font=("Currier", 14)).layout(layout)


while True:
    botao, valores = janela.Read()
    if botao in ("Sair", sg.WIN_CLOSED):
        break
    elif botao == "Calcular":
        valor = float(valores[0])
        resultado = sqrt(valor)
        janela["Resultado"].Update(f"{resultado:.2f}")
    else:
        pass

janela.close()
