import PySimpleGUI as sg
from faker import Faker
from funcionalidades import novo_contato, limpar_campos, listar_contatos, buscar

f = Faker("pt_BR")

agenda = []

sg.theme("LightGrey1")

layout_esquerda = [
    [sg.Text("Agenda App", font=("Helvetica", 20))],
    [sg.Text("Nome:", size=(8, 1)), sg.InputText(key="-NOME-")],
    [sg.Text("Telefone:", size=(8, 1)), sg.InputText(key="-TELEFONE-")],
    [sg.Text("Email:", size=(8, 1)), sg.InputText(key="-EMAIL-")],
    [sg.Text("Endereço:", size=(8, 1)), sg.InputText(key="-ENDERECO-")],
]

layout_direita = [
    [sg.Push(), sg.Text("Contatos", font=("Helvetica", 20)), sg.Push()],
    [sg.Listbox(values=agenda, size=(15, 6), key="-LISTA-", enable_events=True)],
]

layout = [
    [sg.Column(layout_esquerda), sg.Column(layout_direita)],
    [
        sg.Push(),
        sg.Button("Adicionar", size=(12, 1)),
        sg.Button("criarContato", size=(12, 1)),
        sg.Button("sair", size=(12, 1)),
        sg.Push(),
    ],
]

janela = sg.Window("Agenda App", layout, font=("Helvetica", 14))

while True:
    eventos, valores = janela.read()

    if eventos in (sg.WIN_CLOSED, "sair"):
        break
    if eventos == "criarContato":
        nome = f.name()
        tel = f.phone_number()
        endereco = f.address()
        email = f.email()
        janela["-NOME-"].update(nome)
        janela["-TELEFONE-"].update(tel)
        janela["-EMAIL-"].update(email)
        janela["-ENDERECO-"].update(endereco)

    if eventos == "Adicionar":
        nome = valores["-NOME-"]
        tel = valores["-TELEFONE-"]
        endereco = valores["-ENDERECO-"]
        email = valores["-EMAIL-"]
        novo_contato(agenda, nome, tel, endereco, email)
        lista_nomes = listar_contatos(agenda)
        janela["-LISTA-"].update(lista_nomes)
        limpar_campos(janela)
        for contato in agenda:
            print()
            print(contato)

    if eventos == "-LISTA-":
        nome = janela["-LISTA-"].get()[0]
        valores = buscar(agenda, nome)
        janela["-NOME-"].update(valores["nome"])
        janela["-TELEFONE-"].update(valores["telefone"])
        janela["-EMAIL-"].update(valores["email"])
        janela["-ENDERECO-"].update(valores["endereco"])

janela.close()

# TODO
# 1. Adicionar a funcionalidade de apagar um contato
# 2. Adicionar a funcionalidade de editar(UPDATE) um contato
# 3. analisar o design do app e melhorar
# 4. criar o instalador do app
# 5. tirar o codigo do faker na versao final ( beta)
