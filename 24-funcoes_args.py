'''
*args - Utilizamos ele quando não temos certeza de quantos argumentos queremos ter numa função

- Os argumentos são passados como uma tupla


**Kwargs - utilizamos quando queremos passar não só os valores mas também as respectivas chaves
- Os argumentos são como um dicionário
'''

# Soma de números
def sum(*num):
    sum_total = 0
    for i in num:
        sum_total += i
        print(f"A soma é: {sum_total}")

sum(10,20,30)


#Apresentação de cursos

def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")


presentation(Name = "Python", Category = "Backend", Level = "Iniciante")
