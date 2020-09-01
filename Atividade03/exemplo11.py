# Substitui o placeholder "0" usando o primeiro argumento da função format
# usando uma largura mínima de 4 caracteres
print("{0:4}".format(-123))
# Substitui o placeholder "0" usando o primeiro argumento da função format
# e formata a string adicionando uma largura mínima de 4 caracteres
print("{0:4}".format(123))
# Substitui o placeholder "0" usando o primeiro argumento da função format
# e formata a string adicionando 4 caracteres de largura mínima e 2 caracteres de
# precisão como valor em ponto flutuante
print("{0:4.2f}".format(33.3287))
# Substitui o placeholder "0" usando o primeiro argumento da função format
# e formata a string usando sinal e adicionando 4 caracteres de largura mínima e
# 2 caracteres de precisão em ponto flutuante
print("{0:+4.2f}".format(33.3287))
# Substitui o placeholder "0" usando o primeiro argumento da função format
# e formata a string usando sinal e adicionando 4 caracteres de largura máxima
# 2 caracteres de precisão em exponencial
print("{0:+4.2e}".format(33.3287))
# Substitui o placeholder "0" usando o primeiro argumento da função format
# e formata a string em número binário
print("{0:b}".format(123))