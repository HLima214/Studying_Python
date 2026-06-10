#1 - Liste valores de 0 a 10 que sejam menor do que 4

listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

#2 - Jogos que possuem a letra A

gameList = ["Mario Odyssey", "Far Cry", "Read Dead 2",
            "Kirby", "Zelda"]

newList = [a for a in gameList if "a" in a ]
print(newList)


#3-Jogos que eu zerei
gamesFinished = [x for x in gameList if x != "Read Dead 2"]
print(gamesFinished)