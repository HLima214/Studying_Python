print("Substituindo caractere repetido")

gameName = "fifa 26"

print(gameName[0] + gameName[1:].replace("f", "$"))

print("="*10)

print("Troca de caracteres")

word1 = "def"
word2 = "ghi"

print(word1.replace(word1[:2],word2[:2]))
print(word2.replace(word2[:2],word1[:2]))