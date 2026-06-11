# 1- Função de potência de números
power = lambda num: num**2

# 2- Função que verifica se o número é par
pair = lambda number: number % 2 == 0

# 3- Função que divide um número por outro
division = lambda x,y: x/y


# 4- Função que inverte uma string
invert = lambda phrase: phrase[::-1]


print(power(5))
print(pair(300))
print(division(10,5))
print(invert("AtéCubanos"))