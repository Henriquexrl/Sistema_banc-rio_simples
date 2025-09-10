class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = []

class Conta:
    def __init__(self, agencia, numero, cliente):
        self.agencia = agencia
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def sacar(self, *, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

def criar_usuario(clientes):
    cpf = input("Informe o CPF (somente números): ")
    if any(cliente.cpf == cpf for cliente in clientes):
        print("Já existe usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    cliente = Cliente(nome, cpf, data_nascimento, endereco)
    clientes.append(cliente)
    print("Usuário criado com sucesso!")

def filtrar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

def criar_conta(agencia, numero_conta, clientes, contas):
    cpf = input("Informe o CPF do usuário: ")
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        conta = Conta(agencia, numero_conta, cliente)
        contas.append(conta)
        cliente.contas.append(conta)
        print("Conta criada com sucesso!")
    else:
        print("Usuário não encontrado. Conta não criada.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\nAgência: {conta.agencia}
C/C: {conta.numero}
Titular: {conta.cliente.nome}
"""
        print(linha)

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Novo usuário
[c] Nova conta
[l] Listar contas
[q] Sair

=> """

clientes = []
contas = []
AGENCIA = "0001"

def selecionar_conta(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return None
    print("Selecione o número da conta:")
    for i, conta in enumerate(contas, 1):
        print(f"{i} - {conta.cliente.nome} (Agência: {conta.agencia}, Conta: {conta.numero})")
    try:
        idx = int(input("Número da conta: ")) - 1
        if 0 <= idx < len(contas):
            return contas[idx]
        else:
            print("Conta inválida.")
            return None
    except ValueError:
        print("Entrada inválida.")
        return None

while True:
    opcao = input(menu)

    if opcao == "d":
        conta = selecionar_conta(contas)
        if conta:
            valor = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)

    elif opcao == "s":
        conta = selecionar_conta(contas)
        if conta:
            valor = float(input("Informe o valor do saque: "))
            conta.sacar(valor=valor)

    elif opcao == "e":
        conta = selecionar_conta(contas)
        if conta:
            conta.exibir_extrato()

    elif opcao == "u":
        criar_usuario(clientes)

    elif opcao == "c":
        numero_conta = len(contas) + 1
        criar_conta(AGENCIA, numero_conta, clientes, contas)

    elif opcao == "l":
        listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        