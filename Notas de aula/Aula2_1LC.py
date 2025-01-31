"""
programa exemplo para abrir e fechar arquivo no 
modo binario para gravar(w) e ler(r) dados
"""

import pickle

agenda = []

while True:

    print(
        """
             Agendinha v 0.1
        0 - sair
        1 - novo contato
        2 - listar contatos
        3 - salvar dados
        4 - ler dados
    """
    )

    op = int(input("Opção: "))

    match op:

        case 0:
            print("Saindo...")
            break
        case 1:
            nome = input("Nome: ")
            email = input("Email: ")
            agenda.append([nome, email])
            print(agenda)
        case 2:
            for contato in agenda:
                print(f"Nome: {contato[0]} - Email: {contato[1]}")

        case 3:
            with open("agendaLC.bin", "wb") as arq:
                # wb - write binary - modo de escrita binária
                pickle.dump(agenda, arq)

        case 4:
            with open("agendaLC.bin", "rb") as arq:
                # rb - read binary - modo de leitura binária
                agenda = pickle.load(arq)
        case _:
            print("Opção inválida")
