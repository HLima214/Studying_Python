"""
Fatorial de um número
"""

def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num-1))
number = int(input("Digite um número para fatoriar: \n"))
print(f"O fatorial de {number} é: {factorial(number)}")


# Soma totla de um número

def factorial(num):
    if num == 1:
        return 1
    else:
        return (num + factorial(num-1))
number = int(input("Digite um número para somar: \n"))
print(f"A soma total de {number} é: {factorial(number)}")
