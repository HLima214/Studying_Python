'''
Escreva um módulo para tratar string e que possua as seguintes funcionalidades:

1. Inverter uma string de tras para frente
2. Retornar apenas letras com indice par
3. Retornar apenas letras com indice ímpar
'''

def invert():
    text = input("Digite um frase: \n")
    invertido = text[::-1]
    print(invertido)


#invert()


def pair():
    text = input("Digite uma frase: \n")
    numPar = 0
    for i in text:
        posicao = text.find(i)
        

        if posicao % 2 == 0:
            print(f"Posição par: \n{posicao}")
            numPar += 1
            
    print(f"Total de posições: {posicao}")
    print(f"Quantidade de letras com índice par: {numPar}")



        
        

    

pair()




#if i % 2 == 0:
 #           print(text(i))
#            numPar += 1