name = input("Digite o nome do jogo:\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo:\n"))
classification = float(input("Digite a nota de classificação do jogo:\n"))

if classification > 8:
    print(f"Recomendo jogar {name} !")
else:
    print(f"Não recomendo jogar {name} !")