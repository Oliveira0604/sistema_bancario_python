def verificar(txt):
    while True:
        confirmar = input(f"Opção de {txt} selecionada. Deseja continuar? [S/N]: ").upper().strip()
        if confirmar not in "SN":
            print("Opção inválida. Digite apenas S ou N")
        else:
            break
    return confirmar     

def verificar_valor_erro():
    while True:
        try:
            valor = float(input("Valor: R$: "))
            break
        except ValueError:
            print("Valor inválido")
    return valor

def deposito(txt):
    global saldo
    global extrato
    valor = verificar_valor_erro()
    if valor <= 0:
        print("Valor inválido.")
    else:
        deposito_realizados.append(valor)
        print(f"deposito de número: {len(deposito_realizados)}")
        saldo += valor
        extrato += f"Deposito: R$: {valor:.2f}\n"


def saque(txt):
    global numero_saques
    global saldo
    global extrato
    if numero_saques >= LIMITE_SAQUES:
        print("Você já atingiu seu limite diário de saques.")
        return
    else:
        valor = verificar_valor_erro()
        if valor > 500:
            print("Você pode sacar apenas R$: 500.00 por operação.")
        elif saldo < valor:
            print(f"Você não tem saldo suficiente para a operação. Saldo atual: R$: {saldo:.2f}")
        elif valor <= 0:
            print("Operação inválida.")
        else:
            saques_realizados.append(valor)
            print(f"saque de número: {len(saques_realizados)}")
            numero_saques += 1
            saldo -= valor
            extrato += f"Saque: R$: {valor:.2f}\n"



def verifica_investimento(txt, rendimento):
    global extrato
    global saldo
    print(f"Opção selecionada {txt} renda de {rendimento}% ao ano")
    while True:
        confirmar = input("Deseja continuar com a operação? [S/N]: ").upper().strip()
        if confirmar not in "SN":
            print("Digite apenas S ou N: ")
        elif confirmar == "S":
            try:
                valor = float(input("Valor: R$: "))
                if valor > saldo:
                    print("Você nãpo possui saldo suficiente para completar a operação.")
                    print("Voltando para o menu")
                    break
                elif valor < 10:
                    print("Valor inválido. Minimo R$: 10.00")
                else:
                    saldo -= valor
                    extrato += f"Investimento de R$: {valor:.2f} em {txt}"
                    investimentos.append(valor)
                    break
            except ValueError:
                print("Valor inválido.")
        elif confirmar == "N":
            break
                        
               

def investimento():
    while True:  
        print('''======== Selecione a opção ========
    1: Renda Fixa
    2: Renda Variável
    3: Verificar meus investimentos
          ''')
    
        opcao = input("Opção de investimento: ")
        if opcao not in "123":
            print("Opção inválida")
        
        if opcao == "1":
            print('''======== Investimentos de renda fixa ========
    [a] CDB (Certificado de Depósito Bancário)
    [b] LCI (Letra de Crédito Imobiliário)
    [c] LCA (Letra de Crédito do Agronegócio)
    [d] Tesouro Direto (Tesouro Selic, Tesouro IPCA+, Tesouro Prefixado)
    [e] CRI (Certificado de Recebíveis Imobiliários)
    [f] CRA (Certificado de Recebíveis do Agronegócio)
                  ''')
            opcao = input("Tipo de investimento: ").lower().strip()
            if opcao == "a":
                verifica_investimento("CDB", 12)
                break
            elif opcao == "b":
                verifica_investimento("LCI", 10.05)
            elif opcao == "c":
                verifica_investimento("LCA", 10.50)
            elif opcao == "d":
                verifica_investimento("Tesouro Direto", 12.50)
            elif opcao == "e":
                verifica_investimento("CRI", 11.29)
            elif opcao == "f":
                verifica_investimento("CRA", 11.50)
        elif opcao == "2":
            print('''======== Investimentos de renda variável ========
            *Valores estimados
            [a] Ações
            [b] FIIs (Fundos de Investimento Imobiliário)
            [c] ETFs (Exchange Traded Funds)
            [d] BDRs (Brazilian Depositary Receipts)
            [e] Criptomoedas (Bitcoin, Ethereum, etc.)
                  ''')
            opcao = input("Tipo de investimento: ").lower().strip()
            if opcao == "a":
                verifica_investimento("Ações", 15)
                break
            elif opcao == "b":
                verifica_investimento("FIIs", 10)
                break
            elif opcao == "c":
                verifica_investimento("ETFs", 18)
                break
            elif opcao == "d":
                verifica_investimento("BDRs", 18)
                break
            elif opcao == "e":
                verifica_investimento("Criptomoedas", 500)
                break

            
def poupanca():
    global saldo_poupanca
    global saldo
    global extrato
    print("POUPANÇA".center(20, "="))
    print(f''''
    1: Aplicar
    2: Resgatar
    3: Voltar
    Saldo: R$: {saldo_poupanca:.2f}      ''')
    print("=" * 20)
    while True:
        opcao_poupanca = input("Opção poupança: ")
        if opcao_poupanca not in "123":
            print("Opção inválida")
        elif opcao_poupanca == "1":
            print(f"Aplicação\nSaldo conta corrente: R$: {saldo:.2f}\nSaldo conta poupança: R$: {saldo_poupanca:.2f}")
            valor_aplicacao = verificar_valor_erro()
            if valor_aplicacao > saldo:
                print(f"Saldo insuficiente para completar a transação.\nSeu saldo é de {saldo:.2f}")
            else:
                saldo -= valor_aplicacao
                saldo_poupanca += valor_aplicacao
                extrato += f"Aplicação na poupança: R$ {valor_aplicacao:.2f}\n"
                print(f"Aplicação realizada. Valor: R$:{valor_aplicacao:.2f}")
        elif opcao_poupanca == "2":
            print(f"Saldo conta poupança: R$: {saldo_poupanca:.2f}")
            valor_resgate = verificar_valor_erro()
            if saldo_poupanca <= 0:
                print("Você não possui saldo para resgate.")
                break
            else:
                if valor_resgate > saldo_poupanca:
                    print(f"Saldo insuficiente para resgate.\nSeu saldo é de R$: {saldo_poupanca:.2f}")
                else:
                    saldo_poupanca -= valor_resgate
                    saldo += valor_resgate
                    extrato += f"Resgate da poupança: R$: {valor_resgate:.2f}\n"
                    print(f"Resgate realizado com sucesso. Valor: R$: {valor_resgate:.2f}")
        else:
            print("Voltando ao menu.")
            break


menu = """
    Bem-vindo ao DIO Bank. É um prazer ter você aqui com a gente.
    Qual operação deseja realizar?
    [d] Deposito
    [s] Sacar
    [e] Extrato
    [i] Investimento
    [p] Poupança
    [x] Sair 
"""
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""
deposito_realizados = []
saques_realizados = []
investimentos = []
saldo_poupanca = 0

while True:
    opcao = input(menu + "Opção: ").lower()

    if opcao == "d":
        if verificar("deposito") == "S":
            deposito("Deposito") 
    elif opcao == "s":
        if verificar("saque") == "S":
            saque("saque")
    elif opcao == "e":
        print(" EXTRATO ".center(40, "="))
        print(extrato)
        print(f"Saldo: R$: {saldo:.2f}")
        print("=" * 40)
    elif opcao == "i":
        if verificar("investimento") == "S":
            investimento()
    elif opcao == "p":
        if verificar("poupança") == "S":
            poupanca()
    elif opcao == "x":
        break
    else:
        print("Operação inválida.")