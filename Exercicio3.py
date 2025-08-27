# Entrada de dados do funcionário

print("--- Avaliação de funcionário ---\n")

NomeFuncionario = input("Digite o nome do funcionário: ")
Produtividade = float(input("Digite a produtividade do funcionário(0 a 100): "))
Presenca = float(input("Digite a presença do funcionário(0 a 100%): "))

# Requisitos avaliação funcionário

if Presenca >= 90 and Produtividade >= 80:
  print("Desempenho excelente.")

elif Presenca >= 75 and Produtividade >= 60:
  print("Bom desempenho.")

else:
  print("\nDesempenho insatisfatório.")

print("\n--- Avaliação de funcionário concluída ---")
