gameDescription = """ #Print multilinha
    Fifa 26 é um jogo de futebol
    desenvolvido pela EA
    e que possibilita jogar online ou localmente
"""

gameName = "Fifa"
gameVersion = " 23"
line = "="


#1-Concatenação de strings
print(f"O nome do jogo é: {gameName + gameVersion}")

#2-Multiplicação de strings
print(line * 25)

#3-Procurar uma palavra no texto
print("Fifa" in gameDescription)
print("fifa" in gameDescription)
print("online" in gameDescription)
