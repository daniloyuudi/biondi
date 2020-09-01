# Cria uma string
s = "Teste String"
# Substitui o placeholder "0" com o primeiro argumento da função format e formata
# a string com um tamanho mínimo de 20 caracteres, adicionando espaços em branco e
# alinha a string original à direita
print("{0:>20}".format(s))
# Substitui o placeholder "0" com o primeiro argumento da função format e formata
# a string com um tamanho mínimo de 20 caracteres, alinhando a string à direita e
# adicionando o caractere "#" se necessário
print("{0:#>20}".format(s))
# Substitui o placeholder "0" com o primeiro argumento da função format e formata
# a string ao centro com o tamanho mínimo de 20 caracteres adicionando espaços em
# branco se necessário
print("{0:^20}".format(s))
# Substitui o placeholder "0" pelo primeiro argumento da função format e formata
# a string adicionando um tamanho máximo de 5 caracteres
print("{0:.5}".format(s))