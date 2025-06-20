def deposito(text):
    while True: #um loop para veirificar se a pessoa realmente deseja fazer deposito ou voltar
            confirma = input(f"Opção selecionada: {text}\nDigite S para confirmar ou X para voltar ao menu: ").upper()

            if confirma not in "SX": #uma condição para verificar se a pessoa está digitando algo diferente do que é pedido, e se sim, ficará repetindo até o que digite corretamente.
                confirma = input(f"Opção selecionada: {text}\nDigite S para confirmar ou X para voltar ao menu: ").upper()
            elif confirma == "X": #se a pessoa digitar o X volta quebra o laço e volta para o menu.
                break
            elif confirma == "S":
                global saldo
                valor = float(input("Valor R$: "))
                if valor <= 0:
                    print("Valor inválido.")
                else:
                    deposito_realizados.append(valor)
                    print(f"deposito de número: {len(deposito_realizados)}")
                    saldo += valor


def saque(text):
    while True: #um loop para veirificar se a pessoa realmente deseja fazer deposito ou voltar
        confirma = input(f"Opção selecionada: {text}\nDigite S para confirmar ou X para voltar ao menu: ").upper()

        if confirma not in "SX": #verifica se a pessoa está digitando corretamente, e repete se não
            confirma = input(f"Opção selecionada: {text}\nDigite S para confirmar ou X para voltar ao menu: ").upper()
        elif confirma == "X": #se a pessoa digitar o X volta quebra o laço e volta para o menu.
            break
        elif confirma == "S":
            global numero_saques
            if numero_saques >= LIMITE_SAQUES:
                print("Você já atingiu seu limite diário de saques.")
                break
            else:
                global saldo
                valor = float(input("Valor R$: "))
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
                

def extrato():
    print("=========== EXTRATO ===========")
    print(f"Operações realizadas")
    for indice, deposito in enumerate(deposito_realizados):
        print(f"{indice + 1}º deposito: R$: {deposito:.2f}")
    
    for indice, saque in enumerate(saques_realizados):
        print(f"{indice + 1}º saque: R$: {saque:.2f}")

    print(f"Seu saldo atual é de: R$: {saldo:.2f}")
    print("=" * 31)

menu = """
    Bem-vindo ao DIO Bank. É um prazer ter você aqui com a gente.
    Qual operação deseja realizar?
    [d] Deposito
    [s] Sacar
    [e] Extrato
    [x] Sair 
"""
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
deposito_realizados = []
saques_realizados = []

while True:
    opcao = input(menu + "Opção: ").lower()

    if opcao == "d":
        deposito("Deposito") 
    elif opcao == "s":
        saque("saque")
    elif opcao == "e":
        extrato()
    elif opcao == "x":
        break
    else:
        print("Operação inválida.")