# Cria um dicionário com algumas entradas
d = {'gato': 'cat', 'cachorro': 'dog' }
# Exibe o valor da chave 'gato' do dicionário
print(d['gato'])
# Exibe se a chave 'gato' está no dicionário
print('gato' in d)
# Exibe o dicionário d
print(d)
# Cria uma nova chave 'peixe' no dicionário d com o valor 'fish'
d['peixe'] = 'fish'
# Exibe o valor da chave 'peixe' no dicionário d
print(d['peixe'])
# Exibe uma mensagem de erro pois a chave 'macaco' não existe no dicionário d
print(d['macaco'])
# Exibe o valor da chave 'macaco' no dicionário d ou 'N/A' se a chave não existir
print(d.get('macaco', 'N/A'))
# Exibe o valor da chave 'peixe' no dicionário d ou 'N/A' se a chave não existir
print(d.get('peixe', 'N/A'))
# Remove a chave 'peixe' do dicionário d
del d['peixe']
# Exibe a chave 'peixe' do dicionário d ou 'N/A' se a chave não existir
print(d.get('peixe', 'N/A'))