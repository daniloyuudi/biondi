# Pega o input do usuário com uma mensagem e converte para float
nota = float(input("Digite sua nota na disciplina:"))
# Testa se o valor da variável nota é menor do que 6
if nota < 6.0:
  # Exibe uma mensagem notificando que o aluno foi reprovado
  print('Reprovado!')