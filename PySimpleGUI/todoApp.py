import PySimpleGUI as sg


def gerenciador_tarefas():
    tarefas = []

    layout = [
        [sg.Input(key="-TAREFA-", size=(30, 1)), sg.Button("Adicionar")],
        [sg.Listbox(values=tarefas, size=(40, 10), key="-LISTA-")],
        [sg.Button("Remover"), sg.Button("Limpar Tudo")],
    ]

    window = sg.Window("Gerenciador de Tarefas", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "Adicionar" and values["-TAREFA-"]:
            tarefas.append(values["-TAREFA-"])
            window["-LISTA-"].update(tarefas)
            window["-TAREFA-"].update("")

        if event == "Remover" and values["-LISTA-"]:
            tarefa_selecionada = values["-LISTA-"][0]
            tarefas.remove(tarefa_selecionada)
            window["-LISTA-"].update(tarefas)

        if event == "Limpar Tudo":
            tarefas.clear()
            window["-LISTA-"].update(tarefas)

    window.close()


if __name__ == "__main__":
    gerenciador_tarefas()
