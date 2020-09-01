# Cria um dicionário usando um loop for
d = {(x, x + 1): x for x in range(10)}
# Exibe dicionário d na tela
print(d)
# Cria uma tupla tp2
tp2 = (5, 6)
# Exibe o tipo da variável tp2
print(type(tp2))
# Exibe o valor da chave do dicionário d igual ao valor da variável tp2
print(d[tp2])
# Exibe o valor com a chave (1, 2) no dicionário d
print(d[(1, 2)])