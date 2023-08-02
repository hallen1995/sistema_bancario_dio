def menu():
    print(" BEM VINDO AO BANCO DO DESAFIO ".center(50, "-") + "\n" )
    print(" MENU DE OPERAÇÕES ".center(50,"-") + "\n")
    print("  [01] Saque")
    print("  [02] Depósito")
    print("  [03] Extrato")
    print("  [04] Finalizar Operação\n")
    
menu()

saldo = 0
extrato = ""
limite_valor_saque = 500
numero_saques = 0
LIMITE_SAQUES = 3


def realizando_saque():
    global saldo,extrato, limite_valor_saque, numero_saques
    print("Você optou pelo Saque")
    valor_saque = float(input("Digite o valor do Saque:\n >> R$"))
    
    if valor_saque > 0:
        if numero_saques < LIMITE_SAQUES:
            if valor_saque <= saldo:
                saldo -= valor_saque
                extrato +=f"Saque: R$ {valor_saque:.2f}\n"
            
            else:
                print("Saldo insuficiente para o saque.")
        else:
            print("Limite de saques diários atingido.")
    else:
        print("Valor do saque inválido.")


def realizando_deposito():
    global saldo, extrato
    print("Você optou pelo Depósito")
    valor_deposito = float(input("Digite o valor do Depósito:\n >> R$"))
    
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
    else:
        print("Valor do depósito inválido.")


def consulta_extrato():
    global extrato, saldo
    print("Você optou pelo Extrato")
    print(" Extrato :".center(50, "="))
    print(extrato)
    print(f"Saldo Atual: R$ {saldo:.2f}")
    print("".center(50,"="))


def finalizando_operacao():
    print("Finalizando a operação!")
    exit()

opcoes = {
1 : realizando_saque,
2 : realizando_deposito,
3 : consulta_extrato,
4 : finalizando_operacao
}
    
while True:
    try:
        opcao = int(input("Escola a operação desejada:"))
    except ValueError:
        print("Valor incorreto. Por favor, insira um número inteiro.")
        continue
        
    funcao_escolhida = opcoes.get(opcao)
    if funcao_escolhida:
        funcao_escolhida()
    else:
        print("Opção Inválida, escolha uma opção válida do menu")
    
print("Obrigado por utilizar o Banco dos Desafios!")
    
