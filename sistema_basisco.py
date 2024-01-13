menu = """
  [d] Depositar
  [s] Saque
  [e] Extrato 
  [f] Finalizar 
Opção :  """

saldo = 0
SAQUE_MAXIMO = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def deposito():
  global saldo
  try:
    
      valor = int(input("\nQual o valor a ser Depositado: "))
      if valor > 0:
        saldo += valor
        extrato.append(f"Deposito: R${valor:.2f} - Saldo atual: R${saldo:.2f} ")


  except ValueError:
    print("Valor informado não é valido!!")

def saque():
  global saldo, numero_saques
  try:
    valor = int(input("\nQual o valor que deseja sacar: "))
    
    excedeu_valor = valor > saldo

    excedeu_limite = valor > SAQUE_MAXIMO

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_valor:
      print("O valor solicitado é maior que o saldo na conta!")
    elif excedeu_limite:
      print("O saque não pode ser maior que R$500,00 !!")
    elif excedeu_saques:
      print("Você atingiu o limite de saques diarios!!")
    elif valor > 0:
      saldo -= valor
      numero_saques +=1
      extrato.append(f"Saque: R${valor},00 - Saldo atual: R${saldo:.2f}")

  except ValueError:
    print("Valor informado não é valido!!")

def mostrar_extrato():
  if len(extrato) == 0:
    print("\n=============== EXTRATO ==============")
    print("Não foram realizada movimentações")
  else:
    print("\n=============== EXTRATO ==============")
    for item in extrato:
      print(item)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n======================================")
while True:

  opcao = input(f"\nSelecione uma das aopçoes abaixo : {menu}")

  if opcao == "d":
    deposito()
  elif opcao == "s":
    saque()
  elif opcao == "e":
    mostrar_extrato()
  elif opcao == "f":
    break
  else: 
    print("Opçao invalida!!")

