#Função para imprimir Hello Wolrd
def wellcome():
    print("Hello Wolrd")
    
wellcome()


# Função para somar dois números
def sum():
    return 5 + 4

print(sum()) # Quando a função estiver com return vc deve utilizar o print para chamar a função caso contrário apenas escreva o nome da função


#Função para cadastrar jogo
def create_game():
    name = input("Digite o nome do jogo:\n")
    yearLaunch = int(input("Digite a data de lançamento do jogo: \n"))
    gamePrince = float(input("Digite o preço do jogo:\n"))
    noteRating = float(input("Digite a nota de avalição do jogo: \n"))
    
    print(f"{name} - R${gamePrince}")
    
    
create_game()

