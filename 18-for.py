gameList = ["Frag Punk", "Fortnite", "Forza Horizon", 
            "Minecraft", "Tomb Raider"]

# # Iterando valores de uma lista
# for game in gameList:
#     print(game)

# # Quando a condição for atendida, o Loop será encerrado

# for game in gameList:
#     if game == "Forza Horizon":
#         break
#     print(game)


# # Quando a condição for atendida, o Loop vai para a próxima interação

# for game in gameList:
#     if game == "Forza Horizon":
#         continue
#     print(game)


# Sistema de avaliação

gameName = input("Digite o nome do jogo: \n")
gameRating = int(input("Digite quantas notas você quer dar ao jogo: "))

sum = 0

for i in range(gameRating):
    note = float(input("Digite a nota para o jogo: "))
    sum += note

print(f"A avaliação do jogo {gameName} é {sum/gameRating :.2f}")





