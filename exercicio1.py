# Entrada de Dados do cliente

NomeCliente = input("Digite seu nome: ")
IdadeCliente = int(input("Digite sua idade: "))
RendaMensalCliente = float(input("Digite sua renda mensal: "))
ValorDeEmprestimo = float(input("Digite o valor do emprestimo: "))
situaçaoEmprestimo = str

# Verificar Condições do cliente 

if IdadeCliente >= 21 and IdadeCliente <= 65 and RendaMensalCliente >= ValorDeEmprestimo*3:
    situaçaoEmprestimo = "Emprestimo Aprovado"
else:
    situaçaoEmprestimo = "Emprestimo Negado"

print("\n================================================2")
print(f"\nCliente: {NomeCliente}")
print(f"Valor de parcela: {ValorDeEmprestimo/10:.2f} ")
print(f"Situação: {situaçaoEmprestimo}")

# Mensagem personalizada dependendo da situação 

match situaçaoEmprestimo:
    case "Emprestimo Aprovado":
        print("Parabèns seu Empreéstimo foi aceito com sucesso")
    case "Emprestimo Negado":
        print("Seu Empréstimo foi negado")
