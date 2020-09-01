# Define uma função potencia com dois parâmetros
def potencia(a,b):
  # Cria um variável c elevando a à potência b
  c = a**b
  # Retorna o valor da variável c
  return c

# Obtêm o valor da variável x do input do usuário e converte para int
x = int(input("Digite um valor:"))
# Obtêm o valor da variável y do input do usuário e converte para int
y = int(input("Digite o valor de potência:"))
# Exibe o resultado da chamada de função potencia passando x e y como argumentos
print(potencia(x,y))