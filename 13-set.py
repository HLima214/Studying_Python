gameSet = {"Fifa 23", "Read Dead 2", "Forza Horizon",
           "Frag Punk", "The Legend Of Zelda"}

print(gameSet)

#Na tupla e no set não pode repetir valores
#No set não é possivel recuperar valores via fatiamento ou slice

# Buscar tamanho do set
print(len(gameSet))

# True e 1 são considerados o mesmo valor

exampleSet = {"Fifa 26", True, 1, 300.00}
print(exampleSet)

#Adicionar item de outro set

gameSet.update(exampleSet)
print(gameSet)

#Remover um item no setr
gameSet.remove(True)
gameSet.remove(300.00)
gameSet.remove("Fifa 26")
print(gameSet)

