# #Calculo de distância

# distanciaPercorrida = float(input("Digite a distância percorrida: \n"))

# if distanciaPercorrida <= 200:
#     precoPassagem = distanciaPercorrida * 0.50
# else:
#     precoPassagem = distanciaPercorrida * 0.35

# print(f"O preço da passagem é R${precoPassagem}")


#Aumento salário funcionario

salarioFuncionario = float(input("Digite o valor do seu salário: \n"))

if salarioFuncionario > 1250.00:
    aumento = salarioFuncionario * 0.10
    print(f"Seu salário aumentou 10% - Valor do novo salário: {salarioFuncionario + aumento}")
else:
    aumento = salarioFuncionario * 0.15
    print(f"Seu salário aumentou 15% - Valor do novo salário: {salarioFuncionario + aumento}")