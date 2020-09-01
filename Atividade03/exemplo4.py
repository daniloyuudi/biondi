# Cria um dicionário d usando tuplas como chaves
d = {(0,1): 0, (1,2): 1, (2,3): 2, (3,4): 3, (4,5): 4,
    (5,6): 5, (6,7): 6, (7,8): 7, (8,9): 8, (9,10): 9}
# Exibe o dicionário d
print(d)
# Cria uma tupla tp2
tp2 = (5,6)
# Exibe o tipo da tupla tp2
print(type(tp2))
# Exibe o valor da chave igual ao valor da variável tp2 no dicionário d
print(d[tp2])
# Exibe o valor da chave (1,2) no dicionário d
print(d[(1,2)])