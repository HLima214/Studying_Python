# Contagem regressiva 
import winsound # módulo de reprodução sonora
contagem = 10

while contagem >= 0:
    print(contagem)
    contagem -= 1

winsound.Beep(500, 500)


# Tabuada

number = int(input("Digite um número: \n"))


print("====TABUADA====")
for multiplo in range(11):
    print(f"{number} x {multiplo} = {number * multiplo}")
    
    
    
# Tabuada diferente maneira de fazer

numero = int(input("Digite um número: \n"))
begin = int(input("De: \n"))
end = int(input("Até: \n"))


while begin <= end:
    print(f"{numero} x {begin} = {numero * begin}")
    begin += 1



