'''Escreva um programa em python que realize o gerenciamento de jogadores. Ele deve atender aos seguintes requisitos:

- Adicionar um time
- Remover um time
- Listar times
- Adicionar jogador em um time
- Remover jogador de um time
- Listar jogadores de um time

1. A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.

2. A opção de adicionar um time deve pedir um nome para o time que será cadastrado.

3. A opção de remover um time deve pedir o índice específico do time que foi cadastrado para fazer a sua exclusão.

4. A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar
 com o nome do jogador que será adicionado.

5. A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e 
utilizar esse índice para remover o jogador que fora cadastrado no time.

6. A opção de listar os jogadores de um time deve ser informado o índice de um time 
e listar os jogadores que foram associados a ele.

Este é o exercício de revisão do módulo, então aproveite para utilizar todos os recursos vistos até agora, 
como os funções, condições, loop, listas, etc.
'''
teams = {}
option = 0


def listTeams():
    print("Listando times:")
    for i,team in enumerate(teams.values()):
        print(f"{i + 1}. {team['nome']} ({len(team['players'])} jogadores)")






    

while(option != 7):
    print("\n====Gerenciador de times====")
    print("Selecione uma das opções abaixo \n")
    print("1. Adicionar um time ")
    print("2. Listar times ")
    print("3. Remover um time ")
    print("4. Adicionar jogador em um time ")
    print("5. Remover jogador de um time ")
    print("6. Listar jogadores de um time ")
    print("7. Sair")

    option = int(input("Selecione uma das opções acima: \n"))

   


    if option == 1:
        teamName = input("Digite o nome do time que deseja adicionar: ")
        teams[teamName] = {'nome': teamName, 'players':[]}

    elif option == 2:
        listTeams()

    elif option == 3:
        listTeams()
        del_option = int(input("Digite o índice do time que deseja remover: \n"))
        if del_option <= len(teams):
            teamName = list(teams.keys())[del_option - 1]
            del teams[teamName]
            print("Time removido")

    elif option == 4:
        listTeams()
        add_player = int(input("Digite o índice do time que deseja adicionar jogador: \n"))
        if add_player <= len(teams):
            teamName = list(teams.keys())[add_player - 1]
            name_player = input(f"Digite o nome do jogador a ser adicionado no time {teamName}: ")
            teams[teamName]['players'].append(name_player)
            listTeams()

    elif option == 5:
        listTeams()
        select_team = int(input("Digite o índice do time que deseja remover jogador: \n"))
        if select_team <= len(teams):
            teamName = list(teams.keys())[select_team - 1]
            players = teams[teamName]['players']

            print(f"Jogadores do time {teamName}:")
            for i, player in enumerate(players):
                print(f"{i + 1}. {player}")
            delete_player = int(input(f"Digite o índice do jogador que deseja remover do time {teamName}: \n"))
            teams[teamName]['players'].pop(delete_player - 1)
            print(f"Jogador removido")

        

    elif option == 6:
        listTeams()
        show_players = int(input("Digite o índice do time que deseja listar os jogadores: \n"))
        if show_players <= len(teams):
            teamName = list(teams.keys())[show_players - 1]
            players = teams[teamName]['players']

            print(f"Jogadores do time {teamName}:")
            for i, player in enumerate(players):
                print(f"{i + 1}. {player}")

            


    elif option == 7:
        break
    
    else:
        print("Opção inválida")





