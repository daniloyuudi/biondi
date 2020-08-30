# cria uma lista com 4 elementos e atribui à variável xs
xs = [3,1,2,'texto']
# exibe o valor da variável xs e o valor do terceiro elemento da lista atribuída à variável xs
print(xs, xs[2])
# exibe o último elemento da lista xs
print(xs[-1])
# atribui a string 'texto' ao terceiro elemento da variável xs
xs[2] = 'texto'
# exibe o valor da variável xs
print(xs)
# adiciona a string literal 'outro' à lista xs
xs.append('outro')
# exibe o novo valor da lista xs
print(xs)
# remove o último valor da lista xs e retorna esse valor
x = xs.pop()
# exibe o valor de x e da lista xs na tela
print(x, xs)
# atribui uma lista à variável animais
animais = ['gato','cachorro','macaco']
# intera sobre os elementos da lista animais e exibe o valor de cada um dos elementos na tela
for animal in animais:
  print(animal)