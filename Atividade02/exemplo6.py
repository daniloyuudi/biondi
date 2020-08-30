# cria dicionário com vários valores numéricos
Precos = {'lapis': 5.5, 'borracha': 7.0, 'caneta': 6.5}
# exibe o dicionário Precos na tela
print(Precos)
# exibe o valor da chave "borracha" na tela
print("O preco da borracha eh:", Precos['borracha'])
# exibe todas as chaves na tela
print(Precos.keys())
# exibe todos os valores na tela
print(Precos.values())
# exibe na tela se a chave 'caneta' existe no dicionário
print('caneta' in Precos)
# exibe na tela se a chave 'caderno' existe no dicionário
print('caderno' in Precos)
# remove a entrada 'borracha'
del Precos['borracha']
# exibe o dicionário Precos na tela
print(Precos)