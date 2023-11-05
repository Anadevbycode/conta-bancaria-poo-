class Cliente:
    def __init__(self, nome, idade, agencia):
        self.nome = nome
        self.idade = idade
        self.agencia = agencia
        self.conta = None

    def abrir_conta(self, numero_conta, saldo_inicial):
        self.conta = Conta(numero_conta, saldo_inicial)

    def __str__(self):
        return f"Cliente: {self.nome}\nIdade: {self.idade}\nBanco: {self.agencia}\nConta: {self.conta.numero_conta}\nSaldo: R${self.conta.saldo:.2f}"

class Conta:
    def __init__(self, numero_conta, saldo_inicial=0.0):
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial
        self.transacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Depósito: +R${valor:.2f}")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.transacoes.append(f"Saque: -R${valor:.2f}")
        else:
            print("Saldo insuficiente.")

    def extrato(self):
        print(f"Extrato da conta {self.numero_conta}:")
        for transacao in self.transacoes:
            print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}")

def menu():
    print("Bem-vindo ao sistema bancário!")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    agencia = input("Digite o nome do banco: ")
    numero_conta = input("Digite o número da conta: ")
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))

    cliente = Cliente(nome, idade, agencia)
    cliente.abrir_conta(numero_conta, saldo_inicial)

    while True:
        print("\nOpções:")
        print("1. Visualizar Extrato")
        print("2. Sacar")
        print("3. Depositar")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cliente.conta.extrato()
        elif escolha == "2":
            valor = float(input("Digite o valor que deseja sacar: "))
            cliente.conta.sacar(valor)
        elif escolha == "3":
            valor = float(input("Digite o valor que deseja depositar: "))
            cliente.conta.depositar(valor)
        elif escolha == "4":
            print("Obrigado por utilizar nosso sistema bancário. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu()
