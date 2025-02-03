import PySimpleGUI as sg


def main():
    # Lista todos os temas disponíveis
    temas = sg.theme_list()

    # Layout da janela
    layout = [
        [sg.Text("Temas disponíveis no PySimpleGUI:", font=("Helvetica", 12, "bold"))],
        [sg.Listbox(values=temas, size=(30, 20), key="-LISTA-", enable_events=True)],
        [sg.Text("Tema selecionado:", font=("Helvetica", 10))],
        [sg.Text("", size=(30, 1), key="-SELECIONADO-")],
        [sg.Button("Visualizar Tema"), sg.Button("Sair")],
    ]

    # Criar a janela principal
    janela = sg.Window("Temas PySimpleGUI", layout)

    # Loop de eventos
    while True:
        evento, valores = janela.read()

        if evento == sg.WIN_CLOSED or evento == "Sair":
            break

        if evento == "-LISTA-" and len(valores["-LISTA-"]) > 0:
            tema_selecionado = valores["-LISTA-"][0]
            janela["-SELECIONADO-"].update(tema_selecionado)

        if evento == "Visualizar Tema" and len(valores["-LISTA-"]) > 0:
            tema_selecionado = valores["-LISTA-"][0]
            sg.theme(tema_selecionado)

            # Criar uma janela de exemplo com o tema selecionado
            layout_exemplo = [
                [sg.Text(f"Tema: {tema_selecionado}")],
                [sg.Input("Campo de texto")],
                [sg.Checkbox("Checkbox"), sg.Radio("Radio", 1)],
                [sg.Combo(["Opção 1", "Opção 2", "Opção 3"])],
                [sg.Button("OK"), sg.Button("Cancelar")],
            ]

            janela_exemplo = sg.Window("Exemplo do Tema", layout_exemplo)
            janela_exemplo.read(close=True)

    janela.close()


if __name__ == "__main__":
    main()
