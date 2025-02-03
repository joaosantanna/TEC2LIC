import PySimpleGUI as sg

sg.theme("LightGrey1")  # Add a touch of color

layout = [
    [sg.Text("Digite seu nome endereço e telefone")],
    [sg.Text("Nome", size=(15, 1)), sg.InputText()],
    [sg.Text("Endereço", size=(15, 1)), sg.InputText()],
    [sg.Text("Telefone", size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Button("Sair")],
]

janela = sg.Window("Exemplo Simples", font=("Currier", 14)).layout(layout)

botao, valores = janela.Read()

while True:
    if botao == "Sair":
        break
    if botao == "Submit":
        print(f"botao:{botao} - valores:{valores}")
