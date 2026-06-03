gameName = "Fifa 26"

#Print multilinha
gameDescription = """ 
    Fifa 26 é um jogo de futebol
    desenvolvido pela EA
    e que possibilita jogar online ou localmente
"""


print(gameName.upper()) #Retorna string em maiscúlo
print(gameName.lower()) #Retorna string em minúsculo
print(gameName.capitalize()) #Retorna apenas a primeira letra maiúscula
print(gameName.center(9,"=")) #Retorna string centralizada com base na quantidade de caracteres
print(gameName.find("f")) #Retorna a posição daquele caractere
print(gameDescription.count("f")) #Conta quantos caracteres
print(gameDescription.count("a")) #Conta quantos caracteres
print(gameDescription.replace("Fifa", "Pes")) #Altear um elemento para outro
print(gameDescription.split(","))

