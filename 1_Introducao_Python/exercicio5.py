# Conta letras maiusculas e minusculas
upperLetter = []
lowLetters = []

def count_letters():
    sentence = input("Digite uma frase: \n")
    for i in sentence:
        if i == i.upper():
            upperLetter.append(i)
            print(f"A letra maiscula {i} foi adicionada a lista de maiusculas ")
        else:
            lowLetters.append(i)
            print(f"A letra minuscula {i} foi adicionada a lista de minusculas ")

    print(f"Letras maisculas: {upperLetter}")
    print(f"Existem {len(upperLetter)} letras maiusculas")
    print(f"Letras minusculas: {lowLetters}")
    print(f"Existem {len(lowLetters)} letras minusculas")

count_letters()




#Lista de números pares e impares de uma lista
# pair_list = []
# odd_list = []


# def validate():

#     numero = int(input("Digite um número: \n"))

#     for i in range(numero) :
#         if i % 2 == 0:
#             pair_list.append(i)
#             print(f"Número {i} adicionado na lista dos números pares")
#         else:
#             odd_list.append(i)
#             print(f"Número {i} adicionado na lista dos números impares")
    
#     print("Pares: ", pair_list)
#     print("Ímpares: ", odd_list)

# validate()








