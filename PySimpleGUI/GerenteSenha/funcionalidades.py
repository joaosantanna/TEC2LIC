from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from random import choices
from pickle import dump, load


def gerar_senha(tamanho, maiuscula, minuscula, numero, simbolo):
    caracteres = ""
    if maiuscula:
        caracteres += ascii_uppercase
    if minuscula:
        caracteres += ascii_lowercase
    if numero:
        caracteres += digits
    if simbolo:
        caracteres += punctuation

    senha_char = choices(caracteres, k=tamanho)
    senha = ""
    for c in senha_char:
        senha += c
    return senha


def salvar_conta(contas):
    with open("contas.pkl", "wb") as arquivo:
        dump(contas, arquivo)


if __name__ == "__main__":
    print(gerar_senha(15, True, True, True, True))
