# Define uma função leitura
def leitura():
  # Obtêm o valor da variável nome como input do usuário
  nome = input("Digite seu nome:")
  # Obtêm o valor da variável sobrenome como input do usuário
  sobrenome = input("Digite seu nome:")
  # Concatena as strings nome, sobrenome e uma string literal
  nomecompleto = nome + " " + sobrenome
  # Exibe o nome completo
  print("Seu nome completo eh:", nomecompleto)

# Chamada da função leitura
leitura()