num1 = float(input("Digite um número: \n"))
num2 = float(input("Digite outro número: \n"))

operation = input("Digite a operação a realizar (+ - * /)\n")

if operation == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
    
elif operation == "-":
    print(f"{num1} - {num2} = {num1 - num2}")

elif operation == "*":
    print(f"{num1} * {num2} = {num1*num2}")

elif operation == "/":
    print(f"{num1} / {num2} = {num1 / num2}")

else:
    print("Opção inválida, tente novamente !")


