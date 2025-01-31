"""
programa exemplo para abrir e fechar arquivo no 
modo text para gravar(w) e ler(r) dados
"""

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
            with open("agendaLC.txt", "w") as arq:
                # w de Write - escrever dados no arquivo
                for contato in agenda:
                    arq.write(contato[0] + "," + contato[1] + "\n")

        case 4:
            with open("agendaLC.txt", "r") as arq:
                # r de Read - ler dados do arquivo
                texto = arq.readlines()
                for linha in texto:
                    contato = linha.strip().split(",")
                    agenda.append(contato)

        case _:
            print("Opção inválida")
