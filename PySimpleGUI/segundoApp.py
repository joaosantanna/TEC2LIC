import PySimpleGUI as sg
from math import sqrt

sg.theme("LightGrey1")  # Add a touch of color

layout = [
    [sg.Text("Digite o valor para calcular a raiz Quadrada")],
    [sg.Text("Valor", size=(15, 1)), sg.InputText(key="-VALOR-")],
    [sg.Text("Resultado", size=(15, 1)), sg.InputText(key="-RESULTADO-")],
    [sg.Button("Calcular", size=(10, 1)), sg.Button("Sair", size=(10, 1))],
]

janela = sg.Window("Calculadora de raiz quadrada", layout, font=("Currier", 14))


while True:
    botao, valores = janela.Read()
    if botao in ("Sair", sg.WIN_CLOSED):
        break
    elif botao == "Calcular":
        print(f"botao:{botao} - valores:{valores}")
        valor = float(valores["-VALOR-"])
        resultado = sqrt(valor)
        janela["-RESULTADO-"].Update(f"{resultado:.2f}")
        # sg.popup("acabou")
    else:
        pass

janela.close()
