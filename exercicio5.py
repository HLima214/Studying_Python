# Conta letras maiusculas e minusculas


#Lista de números pares e impares de uma lista
pair_list = []
odd_list = []


def validate(*number):
  
    for i in number:
        if i % 2 == 0:
            pair_list.append(number)
            print(f"Número {i} adicionado na lista dos números pares")
        else:
            odd_list.append(number)
            print(f"Número {i} adicionado na lista dos números impares")

validate(5,6,7,8,9,10)









