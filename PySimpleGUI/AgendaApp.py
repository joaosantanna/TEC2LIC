import PySimpleGUI as sg

# Lista para armazenar os contatos
contatos = []
sg.theme("Python")


def criar_janela():
    # Layout da coluna da esquerda (lista de contatos)
    coluna_esquerda = [
        [sg.Text("Lista de Contatos")],
        [sg.Listbox(values=[], size=(30, 10), key="-LISTA-", enable_events=True)],
        [sg.Button("Novo Contato"), sg.Button("Excluir Contato")],
    ]

    # Layout da coluna da direita (detalhes do contato)
    coluna_direita = [
        [sg.Text("Detalhes do Contato")],
        [sg.Text("Nome:"), sg.Input(key="-NOME-", size=(30, 1))],
        [sg.Text("Telefone:"), sg.Input(key="-TELEFONE-", size=(30, 1))],
        [sg.Text("Email:"), sg.Input(key="-EMAIL-", size=(30, 1))],
        [sg.Text("Endereço:"), sg.Input(key="-ENDERECO-", size=(30, 1))],
        [sg.Button("Salvar"), sg.Button("Limpar")],
    ]

    # Layout principal com as duas colunas
    layout = [[sg.Column(coluna_esquerda), sg.VSeparator(), sg.Column(coluna_direita)]]

    return sg.Window("Agenda de Contatos", layout, font=("Helvetica", 16))


def limpar_campos(window):
    window["-NOME-"].update("")
    window["-TELEFONE-"].update("")
    window["-EMAIL-"].update("")
    window["-ENDERECO-"].update("")


def atualizar_lista(window):
    window["-LISTA-"].update([contato["nome"] for contato in contatos])


def main():
    window = criar_janela()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "Novo Contato":
            limpar_campos(window)

        if event == "Limpar":
            limpar_campos(window)

        if event == "Salvar":
            novo_contato = {
                "nome": values["-NOME-"],
                "telefone": values["-TELEFONE-"],
                "email": values["-EMAIL-"],
                "endereco": values["-ENDERECO-"],
            }

            # Verifica se está editando um contato existente
            contato_existente = next(
                (i for i, c in enumerate(contatos) if c["nome"] == values["-NOME-"]),
                None,
            )

            if contato_existente is not None:
                contatos[contato_existente] = novo_contato
            else:
                contatos.append(novo_contato)

            atualizar_lista(window)
            limpar_campos(window)

        if event == "-LISTA-" and len(values["-LISTA-"]) > 0:
            nome_selecionado = values["-LISTA-"][0]
            contato = next((c for c in contatos if c["nome"] == nome_selecionado), None)
            if contato:
                window["-NOME-"].update(contato["nome"])
                window["-TELEFONE-"].update(contato["telefone"])
                window["-EMAIL-"].update(contato["email"])
                window["-ENDERECO-"].update(contato["endereco"])

        if event == "Excluir Contato" and len(values["-LISTA-"]) > 0:
            nome_selecionado = values["-LISTA-"][0]
            contatos[:] = [c for c in contatos if c["nome"] != nome_selecionado]
            atualizar_lista(window)
            limpar_campos(window)

    window.close()


if __name__ == "__main__":
    main()
