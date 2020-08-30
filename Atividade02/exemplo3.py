# cria a variável hello e atribui a string 'hello' à variável
hello = 'hello'
# cria a variável world e atribui a string 'world' à variável
world = "world"
# exibe o valor da variável hello na tela
print(hello)
# exibe o tamanho da string hello na tela
print(len(hello))
# cria string concatenando a os valores das variáveis hello, world e de uma string literal
hw = hello + ' ' + world
# exibe o valor de hw na tela
print(hw)
# cria a variável hw12 e atribui uma tupla com 2 strings e 1 valor numérico à format string
hw12 = '%s %s %d' % (hello, world, 12)
# exibe o valor da variável hw12 na tela
print(hw12)
# substitui as chaves na format string pelo valor da variável hello e atribui à variável hw12
hw12 = '() {} []'.format(hello, world, 12)
# exibe of valor da variável hw12 na tela
print(hw12)
# cria a variável s e atribui a string literal 'hello'
s = "hello"
# converte o primero caracter da string para caixa alta
print(s.capitalize())
# converte todos caracteres da string s para caixa alta
print(s.upper())
# justifica a string para 7 caracteres adicionando espaços à esquerda se necessário
print(s.rjust(7))
# centraliza a string adicionando espaços à esquerda ou à direita se necessário
print(s.center(7))
# substitui o caracter 'l' por '(ell)' em todas ocorrências na string s
print(s.replace('l', '(ell)'))
# remove os espaços em branco na string literal e exibe na tela
print('     world'.strip())