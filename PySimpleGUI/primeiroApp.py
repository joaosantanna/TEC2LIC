import PySimpleGUI as sg

sg.theme("LightGrey1")  # Add a touch of color

layout = [
    [sg.Text("Digite seu nome endereço e telefone")],
    [sg.Text("Nome", size=(15, 1)), sg.InputText(key="-NOME-")],
    [sg.Text("Endereço", size=(15, 1)), sg.InputText()],
    [sg.Text("Telefone", size=(15, 1)), sg.InputText()],
    [sg.Button("Processar", size=(10, 1)), sg.Button("Sair", size=(10, 1))],
]

janela = sg.Window("Exemplo Simples", layout, font=("Helvetica", 14))


while True:
    botao, valores = janela.Read()

    if botao == "Sair":
        break
    if botao == "Processar":
        print(f"botao:{botao} - valores:{valores}")
        janela["-NOME-"].update("")  # limpa os campos depois de processar a informacao
        janela[0].update("")
        janela[1].update("")

janela.close()
