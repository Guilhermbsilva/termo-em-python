import random

palavras = ["tabela" , "script", "chaves", "delete", "cedula"]

def jogo():
    print("======= ADIVINHE A PALAVRA! ======\n===== A palavra tem 6 letras =====")

    adivinhar = random.choice(palavras)
    #print(adivinhar)

    while True:
        tentativa = input("Digite sua tentativa: ").lower()

        if len(tentativa) != 6:
            print("A palavra deve ter exatamente 6 letras.")
            continue

        resultado = ""

        for i in range(6):
            if tentativa[i] == adivinhar[i]:
                resultado += f"{tentativa[i].upper()}🟩 "
            elif tentativa[i] in adivinhar:
                resultado += f"{tentativa[i].upper()}🟧 "
            else:
                resultado += f"{tentativa[i].upper()}🟥 "

        print(resultado.strip())

        if tentativa == adivinhar:
            print("Parabéns! Você acertou a palavra!")
            break

def menu():
    while True:
        print("\n======= BEM-VINDO AO TERMO =======")
        print("============ 1- Jogar ============")
        print("============ 2- Sair =============")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            jogo()
        elif escolha == "2":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
