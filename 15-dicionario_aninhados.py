import pprint


gamesDict = {
    "Residente evil 4":{
        "yearLauch":2023,
        "classification": 9.8,
        "genero": ["ação", "aventura"]
    },

    "Mario Odyssey":{
        "yearLauch":2017,
        "classification": 9.2,
        "genero": ["Indie", "aventura"]
    },

    "Rainbow Six Siege":{
        "yearLauch":2017,
        "classification": 8.7,
        "genero": ["Ação", "FPS"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)


# Buscar informmação dentro de um dicionario aninhado
print(gamesDict["Mario Odyssey"]["genero"])

# Adicionar um novo item
gamesDict["Mario Odyssey"]["players"]=1
print(gamesDict["Mario Odyssey"])

#Excluir dicionario
del gamesDict["Mario Odyssey"]
pp.pprint(gamesDict)