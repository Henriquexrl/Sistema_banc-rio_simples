# Menu de opções
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
# Variáveis do sistema
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal
while True:
    
    opcao =input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do depósito"))

        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else: 
            print("Ops! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque:"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Ops! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Ops! Você excedeu o limite de saque.")

        elif excedeu_saques:
            print("Ops! Você já realizou o número máximo de saques.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Ops! O valor informado é inválido.")
    
    elif opcao == "e":
        print("\n----------------EXTRATO----------------")
        print("Movimentações não foram realizadas." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}") 
        print("---------------------------------------")

    elif opcao == "q":
        print("Obrigado! Por utilizar nosso sistema.")
        break

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")

