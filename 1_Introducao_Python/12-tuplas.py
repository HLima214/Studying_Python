gamesTuple = ("Tomb Raider", "Read Dead 2", "Forza Horizon",
              "Frag Punk")

print(gamesTuple)
print(type(gamesTuple))

# Não podemos ordenar valores em uma tupla
# Não podemos adicionar valores em uma tupla
# Não podemos remover valores em uma tupla


# Buscar os dois primeiros itens na tupla
print(gamesTuple[:2])

# Buscar o ultimo item da lista
print(gamesTuple[-1])

# Buscar jogos até uma determinada posição

print(gamesTuple[:3])

# Buscar jogos de uma posição em diante
print(gamesTuple[1:3])

# Recuperar um item da tupla pelo indice
print(gamesTuple.index("Read Dead 2"))