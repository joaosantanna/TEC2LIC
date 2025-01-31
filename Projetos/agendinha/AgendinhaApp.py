from funcionalidades import *
import pickle

agenda = []
with open("agenda.bin", "rb") as arq:
    agenda = pickle.load(arq)


while True:

    print(
        """
                    Agendinha v 0.1
                    30 de janeiro de 2025
                    LIC - UFRA

                    Escolha sua opcao
                    0 - sair
                    1 - Novo Contato
                    2 - Listar contatos
                    3 - Editar contato
                    4 - Deletar contato
                    5 - Buscar contato
                    6 - salvar dados no disco
                    CRUD - Create, Read , Update, Delete
        """
    )

    op = int(input("Opcao :"))

    match op:

        case 0:
            print("Tchau")
            break
        case 1:
            resultado = novo_contato(agenda)
            if resultado == 0:
                print("Contato adicionado com sucesso")

        case 2:
            # listar contatos
            listar_contatos(agenda)

        case 3:
            nome = input("Nome:")
            editar_contato(nome, agenda)

        case 4:
            nome = input("Informe o nome do contato para apagar:")
            apagar(nome, agenda)

        case 6:
            with open("agenda.bin", "wb") as arquivo:
                pickle.dump(agenda, arquivo)
            print("Dados salvos com sucesso")

        case _:
            print("Comando não cadastrado")
