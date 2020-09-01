# Cria uma função que recebe 2 parâmetros
def soma(a,b):
  # Soma os argumentos a e b e armazena na variável c
  c=a+b
  # Retorna a variável c como resultado
  return c

# Obtem o valor x do input do usuário e converte para float
x = float(input("Digite um valor:"))
# Obtem o valor y do input do usuário e converte para float
y = float(input("Digite um valor:"))
# Exibe o resultado da função soma passando x e y como argumentos
print(soma(x,y))