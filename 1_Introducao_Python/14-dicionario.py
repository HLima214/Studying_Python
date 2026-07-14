gameDic = {
    "name":"Fifa 26",
    "yearLaunch":2025,
    "gamePrice": 300.00,
    "classification": 8.75,
    "genero": ["Esporte", "Família"]
}
print(gameDic)
print(len(gameDic))
print(type(gameDic))

# Recuperar um elemento do dicionario
print(gameDic['genero'])
print(gameDic.get("classification"))

# Buscar apenas as chaves do dicionario
print(gameDic.keys())

#Buscar itens do dicionario com chave e valor

print(gameDic.items())

#Adicionar item ao dicionario
gameDic["players"] = "2+ players"
print(gameDic)

#Atualizar item no dicionario
gameDic.update({"players":"1+ players"})
print(gameDic)

#Remover item no dicionario
gameDic.pop("players")
print(gameDic)