def novo_contato(agenda):
    print("Novo contato")
    nome = input("Nome:")
    tel = input("telefone:")
    endereco = input("endereço:")
    email = input("email:")
    contato = {
        "nome": nome,
        "telefone": tel,
        "endereco": endereco,
        "email": email,
    }
    agenda.append(contato)
    return 0  # vai voltar 0 se tudo der certo


def listar_contatos(agenda):
    for contato in agenda:
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Endereço:{contato['endereco']}")
        print(f"Email:{contato['email']}")
        print("-----------------------")
    return 0


def buscar(nome, agenda):
    for posicao, contato in enumerate(agenda):
        if nome.lower() == contato["nome"].lower():
            return posicao
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
