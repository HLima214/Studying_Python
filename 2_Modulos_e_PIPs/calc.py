def sum(a,b):
    result = a + b
    return result

def sub(a,b):
    result = a - b
    return result

def mult(a,b):
    result = a * b
    return result

def div(a,b):
    result = a / b
    return result

option = 0

while option != 5:
    print("====Calculadora====")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    option = int(input("Digite a opção desejada: \n"))


    if option == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"O resultado de {num1} + {num2} é: {sum(num1,num2)}\n")

    elif option == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"O resultado de {num1} - {num2} é: {sub(num1,num2)}\n")

    elif option == 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"O resultado de {num1} * {num2} é: {mult(num1,num2)}\n")

    elif option == 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"O resultado de {num1} / {num2} é: {div(num1,num2)}\n")

    elif option == 5:
        print("Saindo...")

    else:
        print("Opção invalida !!")










