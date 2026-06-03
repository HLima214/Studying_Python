name = input("Digite o nome do jogo:\n")
yearLaunch = int(input("Digite a data de lançamento do jogo:\n"))
gamePrince = float(input("Digite o preço do jogo:\n"))
planIncluded = bool(input("Está incluso no serviço mensal ?\n"))


print("###Dados do Jogo###")
print("===================")
print(f"Nome do jogo: {name} \nAno de lançamento: {yearLaunch} \nPreço do jogo: {gamePrince} \nEstá incluso no plano ? {planIncluded}")