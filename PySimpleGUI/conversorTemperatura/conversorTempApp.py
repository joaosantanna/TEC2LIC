import PySimpleGUI as sg

sg.theme("LightGrey1")


coluna_esquerda = [[sg.Image(source="PySimpleGUI/conversorTemperatura/Termometro.png")]]

coluna_direita = [
    [sg.Text("Conversor de temperatura Celcius x Fahrenheit")],
    [
        sg.Text("Valor"),
        sg.InputText(size=(10, 1), key="-VALOR-"),
        sg.Combo(
            ["Celcius", "Fahrenheit"], default_value="Celcius", key="-TEMPERATURA-"
        ),
    ],
    [sg.Text("Valor Convertido", key="-RESULTADO-")],
    [sg.Button("Converter", size=(10, 1)), sg.Button("Sair", size=(10, 1))],
]

layout = [[sg.Column(coluna_esquerda), sg.Column(coluna_direita)]]

janela = sg.Window("Conversor de Temperatura", layout, font=("Helvetica", 14))

while True:

    botao, valores = janela.Read()

    if botao in ("Sair", sg.WIN_CLOSED):
        break
    if botao == "Converter":
        valor = float(valores["-VALOR-"])
        # print(f"botao : {botao}")
        # print(f" valores = {valores}")
        if valores["-TEMPERATURA-"] == "Celcius":
            # converter de Fahrenheit para celcius
            C = (valor - 32) * 5 / 9
            janela["-RESULTADO-"].update(f"{valor:.2f} Fahrenheit = {C:.2f} Celcius")
        else:
            # converter de celcius para Fahrenheit
            F = valor * 1.8 + 32
            janela["-RESULTADO-"].update(f"{valor:.2f} Celcius  = {F:.2f} Fahrenheit")


janela.close()
