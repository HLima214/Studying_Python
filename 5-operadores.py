num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

#Operadores aritméticos

sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
resto = num1 % num2
exp = num1 ** num2

print(sum)
print(sub)
print(div)
print(mult)
print(f"Resto da divisão de {num1} por {num2} é: {resto}")
print(f"O resultado do {num1} elevado a {num2} é: {exp}\n")


#operadores de comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
biggerEqual = num1 >= num2
smallerEqual = num1 <= num2

print(f"O {num1} é maior ou igual que o {num2} ?: {biggerEqual}")
print(f"O {num1} é menor ou igual que o {num2} ?: {smallerEqual}\n")


#Operadores de atribuição

num1 += 1


print(num1)