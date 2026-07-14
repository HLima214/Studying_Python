gameList = ["Frag Punk", "Fortnite", "Forza Horizon", 
            "Minecraft", "Tomb Raider"]


# Tamanho da lista

print(len(gameList))

# Recuperar um item da lista pelo índice

print(gameList.index("Minecraft"))

# Adicionar item ao final da lista
gameList.append("GTA V")
print(gameList)

# Ordenar lista
print(gameList.sort())

# Copiar itens de uma lista para outra
gameReset = gameList.copy()
gameReset.remove("Tomb Raider")
print(gameReset)


# Remove todos os itens da lista
gameReset.clear()
print(gameReset)