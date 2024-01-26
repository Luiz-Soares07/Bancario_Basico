"""
1- Criar funçoes cadastrar usuario (cliente) e cadastrar conta corrente  (vincular com usuario)
2- A função saque deve receber os argumentos somente por nome (keyword only) - sugestão de argumentos
saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno saldo e extrato
3- A função deposito deve receber os argumentos somente por posição - sugestão argumento(saldo, valor e extrato)
Sugestaoão de retorno: saldo e extrato
4- função extrato deve receber os argumentos por posição(saldo) e nome(extrato)
5- A função criar usuario - deve-se armazenar os usuarios em uma lista, um usuario é composto por: nome,data de 
nascimento, cpf e endereço, o endereço é uma string com o formato: logradouro, nmro - bairro - cidade/sigla estado
deve ser armazenados somente os numeros do cpf. Não se pode cadastrar dois usuarios com o mesmo CPF
6- A função crar conta corrente - deve armazenar as contas em uma lista, uma conta é composta por: agência, numero
da conta e usuario. O numero da conta é sequencial, iniciando em 1. O numero da agência é fixo: "0001. O usuario pode
ter mais de uma conta, mas uma conta pertence a somente um usuario.
"""
import textwrap

menu = """
  [d] Depositar
  [s] Saque
  [e] Extrato
  [c] Cadastro Usuário
  [cc] Cadastro Conta
  [lc] Listar Contas
  [f] Finalizar 
Opção :  """

saldo = 0
extrato = []
users = []
current_accounts = []

def createUser():
  name = input("Informe o nome do usuario: ")
  date_birthday = input("Informe qual a data de nascimento no formato DD/MM/AAAA: ")
  while True:
    cpf = input("Informe o CPF somente em numeros: ")
    if cpf.isnumeric():
      break
    else: 
      continue
  if any(user["CPF"] == cpf for user in users):
    print("Ja existe um usuario vinculado a esse CPF")
  else:
    logradouro = input("Digite o nome da rua: ")
    numero = input("DIgite o numero da residencia: ")
    bairro = input("DIgite o nome do bairro: ")
    cidade_estado = input("Digite a cidade e o estado no formato CC/EE: ")

    address = f"{logradouro}, {numero} - {bairro} - {cidade_estado}"

    user = {"Nome": name,
            "Data de Nascimento": date_birthday,
            "CPF": cpf,
            "Endereço": address}
    
    users.append(user)

    print("Usuario cadastrado com sucesso!")


def createAccount(user):
  current_account = {"Agência": "0001", "Numero da conta": len(current_accounts)+1,"Usuário": user} 
  current_accounts.append(current_account)
  print(f"Conta criada com sucesso para o Usuário: {user}")

  

def withdraw(*, saldo,extrato,SAQUE_MAXIMO = 500,numero_saques = 0,LIMITE_SAQUES = 3):
  try:
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

  return saldo, extrato

def deposit(saldo,valor,extrato, /):
  try:
      if valor > 0:
        saldo += valor
        extrato.append(f"Deposito: R${valor:.2f} - Saldo atual: R${saldo:.2f} ")
  except ValueError:
    print("Valor informado não é valido!!")

  return saldo,extrato

def show_extract(saldo,/, *,extrato):
  if len(extrato) == 0:
    print("\n=============== EXTRATO ==============")
    print("Não foram realizada movimentações")
  else:
    print("\n=============== EXTRATO ==============")
    for item in extrato:
      print(item)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n======================================")

def showAccount(current_accounts):
  if len(current_accounts) == 0:
    print("\n=============== Contas ==============")
    print("Não foram criadas contas ")
  else:
    print("\n=============== Contas ==============")
    for conta in current_accounts:
      linha = f"""\
        Agência: \t{conta['Agência']}
        C/C: \t\t{conta['Numero da conta']}
        Titular: \t{conta['Usuário']["Nome"]}
      """
      print("=" *100)
      print(textwrap.dedent(linha))


while True:

  opcao = input(f"\nSelecione uma das aopçoes abaixo : {menu}")

  if opcao == "d":
    valor = float(input("\nQual o valor a ser Depositado: "))
    saldo, extrato = deposit(saldo,valor,extrato)
  elif opcao == "s":
    valor = float(input("\nQual o valor que deseja sacar: "))
    saldo, extrato = withdraw(saldo=saldo, extrato=extrato)
  elif opcao == "e":
    show_extract(saldo, extrato=extrato)
  elif opcao == "c":
    createUser()
  elif opcao == "cc":
    if not users:
      print("Não existem usuários cadastrados. Cadastre um usuário primeiro.")
    else:
      print("\nLista de Usuários: ")

      for i, user in enumerate(users, start=1):
        print(f"\n{i}. {user['Nome']}")

      escolha = int(input("Escolha um numero correspondente a um usuario: "))
      if 1 <= escolha <= len(users):
        usuario = users[escolha - 1]
        createAccount(usuario)
      else:
        print("Escolha Invalida!")
  elif opcao == "lc":
    showAccount(current_accounts)
  elif opcao == "f":
    break
  else: 
    print("Opçao invalida!!")

  

