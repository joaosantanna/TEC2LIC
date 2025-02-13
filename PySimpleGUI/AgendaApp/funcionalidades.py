def novo_contato(agenda, nome, tel, endereco, email):
    contato = {
        "nome": nome,
        "telefone": tel,
        "endereco": endereco,
        "email": email,
    }
    agenda.append(contato)
    return 0  # vai voltar 0 se tudo der certo


def listar_contatos(agenda):
    lista_nomes = []
    for contato in agenda:
        lista_nomes.append(contato["nome"])
    return lista_nomes


def buscar(agenda, nome):
    for contato in agenda:
        if nome == contato["nome"]:
            return contato
    return -1  # menos 1 significa que eu nao achei o nome na agenda


def apagar(nome, agenda):
    posicao = buscar(nome, agenda)
    if posicao != -1:
        agenda.pop(posicao)
        print("Contato apagado com sucesso")
    else:
        print("Contato não existe na agenda")


def editar_contato(nome, agenda):
    posicao = buscar(nome, agenda)
    if posicao != -1:
        contato = agenda[posicao]
        print("editar nome? (s)(n) :")
        op1 = input("opcao:")
        if op1 == "S" or op1 == "s":
            novo_nome = input("Novo nome:")
            contato["nome"] = novo_nome


def limpar_campos(janela):
    janela["-NOME-"].update("")
    janela["-TELEFONE-"].update("")
    janela["-EMAIL-"].update("")
    janela["-ENDERECO-"].update("")
    return 0
