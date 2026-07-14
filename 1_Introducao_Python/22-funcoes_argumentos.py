# 1 - Crie uma função que receba 2 argumentos: primeiro nome e segundo nome

def full_name(fname, lname):
    print(f"Nome completo: {fname} {lname}")

# Você apenas passa o valor do argumento na hora de chamar a função    
full_name("Henrique", "Lima")


# 2 - Crie uma função que some dois números via parâmetros

def sum (num1, num2):
    print(f"Soma: {num1} + {num2} = {num1 + num2} ")
    
sum(5,4)


# 3 - Argumentos default em uma função
#Voce ja passa o valor do argumento na função
def address(country="Brasil"):
    print(f"Eu moro no: {country}")
    
address()
address("Canadá")

# 4 - Avaliação de jogo

def ratingGame(note):
    print(f"A nota do jogo é: {note}")
    
ratingGame(9.8)
    