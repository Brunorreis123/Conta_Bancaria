class ContaBancaria:
    def __init__(self, nome_titular, numero_conta, saldo_atual):
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self.saldo_atual = saldo_atual
        self.depositos = []
        self.saques = []

    def criar_conta(self):
        self.nome_titular = input("Digite o nome do titular da conta: ")
        self.numero_conta = input("Digite o número da conta: ")
        self.saldo_atual = float(input("Digite o saldo inicial da conta: "))
        self.saques_realizados = 0
        self.limite_diario = 500.0

    def deposito(self, valor):
        if valor > 0:
            self.saldo_atual += valor
            self.depositos.append(valor)
            print("Depósito realizado com sucesso!")
        else:
            print("Não é possível depositar um saldo negativo.")

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo_atual and self.saques_realizados < 3 and valor <= self.limite_diario:
            self.saldo_atual -= valor
            self.saques_realizados += 1
            self.limite_diario -= valor
            self.saques.append(valor)
            print("Saque realizado com sucesso!")
        elif valor > self.limite_diario:
            print("O valor do saque excede o limite diário.")
        else:
            print("Não é possível sacar um valor negativo, superior ao saldo atual ou exceder o limite de saques diários.")

    def extrato(self):
        print("Extrato da conta:")
        print("Nome do titular da conta:", self.nome_titular)
        print("Número da conta:", self.numero_conta)
        print("--- Depositos ---")
        for deposito in self.depositos:
            print("Depósito: R${:,.2f}".format(deposito))
        print("--- Saques ---")
        for saque in self.saques:
            print("Saque: R${:,.2f}".format(saque))
        print("Saldo atual: R${:.2f}".format(self.saldo_atual))

# Programa principal
conta = ContaBancaria("", "", 0.0)

while True:
    print("\n### MENU ###")
    print("1 - Criar conta")
    print("2 - Depósito")
    print("3 - Saque")
    print("4 - Extrato")
    print("5 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        conta.criar_conta()
        print("Conta criada com sucesso!")
    elif opcao == 2:
        valor = float(input("Digite o valor do depósito: "))
        conta.deposito(valor)
    elif opcao == 3:
        valor = float(input("Digite o valor do saque: "))
        conta.saque(valor)
    elif opcao == 4:
        conta.extrato()
    elif opcao == 5:
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
