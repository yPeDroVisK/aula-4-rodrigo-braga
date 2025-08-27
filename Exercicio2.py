# Requisitos para o calculo

print("--- Calculo de equação de 2grau ---\n")

a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))
c = int(input("Digite um numero: "))

# Calcular de Equação de 2grau

delta = b**2 - 4*a*c
x1 = (-b + delta**0.5)/2*a
x2 = (-b - delta**0.5)/2*a

# Verificar condições

if delta < 0:
  print("\nNão exitesm raízes reais.")

elif delta == 0:
  print("\nRaiz única.\n")

else:
  print("\nResultado das duas raízes.")
  print(f"\nRaíz 1: {x1}")
  print(f"Raíz 2: {x2}")
  print("\n--- Calculo concluido ---")
