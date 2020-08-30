# cria uma lista l1 com valores de 0 a 4
l1 = list(range(5))
# exibe os valores de l1 na tela
print(l1)
# cria uma l2 lista com valores entre 3 e 7
l2 = list(range(3,8))
# exibe o valor de l2 na tela
print(l2)
# cria uma lista com valores entre 2 e 10 somando 3 a cada valor da sequência
l3 = list(range(2,11,3))
# exibe o valor de l3 na tela
print(l3)
# cria uma lista l4 combinando as listas l1 e l2
l4 = l1 + l2
# exibe o valor de l4 na tela
print(l4)
# cria uma lista l5 repetindo a lista l3 quatro vezes
l5 = l3 * 4
# exibe a lista l5 na tela
print(l5)
# cria uma lista contendo números, strings e outras listas
l6 = [9, 'texto', 5.7, [16,11,18], "Python", [7,8]]
# exibe a lista l6 na tela
print(l6)
# cria uma lista l7 com os valores dos índices de 1 a 3 da lista l6
l7 = l6[1:4]
# exibe a lista l7 a tela
print(l7)
# cria uma lista l8 com os valores do índice 2 até o último da lista l6
l8 = l6[2:]
# exibe a lista l8 na tela
print(l8)
# cria uma lista l9 com os valores do primeiro índice da lista l6 até o índice 3
l9 = l6[:4]
# exibe a lista l9 na tela
print(l9)