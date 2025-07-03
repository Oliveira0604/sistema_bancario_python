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

def deposito(txt, saldo, extrato, depositos_realizados,/):
    valor = verificar_valor_erro()
    if valor <= 0:
        print("Valor inválido.")
    else:
        depositos_realizados.append(valor)
        print(f"deposito de número: {len(depositos_realizados)}")
        saldo += valor
        extrato += f"Deposito: R$: {valor:.2f}\n"
    return saldo, extrato


def saque(*,txt, saldo, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("Você já atingiu seu limite diário de saques.")
        return
    else:
        valor = verificar_valor_erro()
        if valor > limite:
            print("Você pode sacar apenas R$: 500.00 por operação.")
        elif saldo < valor:
            print(f"Você não tem saldo suficiente para a operação. Saldo atual: R$: {saldo:.2f}")
        elif valor <= 0:
            print("Operação inválida.")
        else:
            numero_saques += 1
            saldo -= valor
            extrato += f"Saque: R$: {valor:.2f}\n"
        return saldo, extrato

def Extrato(saldo,/,*, extrato):
    print(" EXTRATO ".center(40, "="))
    print(extrato)
    print(f"Saldo: R$: {saldo:.2f}")
    print("=" * 40)
    return extrato

def investimento(saldo, extrato, investimentos):
    print("""
    ========== Investimentos ==========
          1: Renda Fixa
          2: Renda Variável
""")
    while True:
        opcao_investimento = input("Digite X para voltar\nOpção: ").upper().strip()
        if opcao_investimento not in "12X":
            opcao_investimento = input("Opção: ")
        elif opcao_investimento == "X":
            return saldo, extrato
        elif opcao_investimento == "1":
            print("Opção selecionada: Renda fixa.\nRendimento de 10% ao ano")
            while True:
                confirma = input("Deseja continuar? [S/N]: ").upper().strip()
                if confirma not in "SN":
                    confirma = input("Deseja continuar? [S/N]: ").upper().strip()
                elif confirma == "N":
                    break
                else:
                    valor = float(input("R$"))
                    if valor <= 0:
                        print("Valor minimo R$10")
                    elif valor > saldo:
                        print("Você não possui saldo suficiente")
                        break
                    else:
                        saldo -= valor
                        extrato += f"Investimento Renda fixa: R${valor:.2f}"
                        investimentos.append(valor)
                        break
        elif opcao_investimento == "2":
            print("Opção selecionada: Renda Variável.\nRendimento variável ao ano")
            while True:
                confirma = input("Deseja continuar? [S/N]: ").upper().strip()
                if confirma not in "SN":
                    confirma = input("Deseja continuar? [S/N]: ").upper().strip()
                elif confirma == "N":
                    break
                else:
                    valor = float(input("R$"))
                    if valor <= 0:
                        print("Valor minimo R$10")
                    elif valor > saldo:
                        print("Você não possui saldo suficiente")
                        break
                    else:
                        saldo -= valor
                        extrato += f"Investimento Renda fixa: R${valor:.2f}"
                        investimentos.append(valor)
                        break
        return saldo, extrato

          
def poupanca(saldo_poupanca, saldo, extrato):
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
                break
            elif valor_aplicacao <= 0:
                print("Valor inválido")
            else:
                saldo -= valor_aplicacao
                saldo_poupanca += valor_aplicacao
                extrato += f"Aplicação na poupança: R$ {valor_aplicacao:.2f}\n"
                print(f"Aplicação realizada. Valor: R$:{valor_aplicacao:.2f}")
                break
        elif opcao_poupanca == "2":
            print(f"Saldo conta poupança: R$: {saldo_poupanca:.2f}")
            valor_resgate = verificar_valor_erro()
            if saldo_poupanca <= 0:
                print("Você não possui saldo para resgate.")
                break
            else:
                if valor_resgate > saldo_poupanca:
                    print(f"Saldo insuficiente para resgate.\nSeu saldo é de R$: {saldo_poupanca:.2f}")
                elif valor_resgate <= 0:
                    print("Valor inválido")
                else:
                    saldo_poupanca -= valor_resgate
                    saldo += valor_resgate
                    extrato += f"Resgate da poupança: R$: {valor_resgate:.2f}\n"
                    print(f"Resgate realizado com sucesso. Valor: R$: {valor_resgate:.2f}")
                    break
        else:
            print("Voltando ao menu.")
            break

def novo_usuario(usuarios):
    cpf = input("CPF (xxx.xxx.xxx-xx): ")
    usuario = filtrar_cpf(cpf, usuarios)
    if usuario == "CPF inválido":
        print("CPF inválido")
        return
    elif usuario == "Usuário já cadastrado":
        print("Usuário já cadastrado")
        return
    else:
        nome = input("Primeiro nome: ").title().strip()
        sobrenome = input("Sobrenome: ")
        data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
        endereco = input("Endereço: Logradouro - nro - bairro - cidade/sigla estado: ")
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("Usuário cadastrado com sucesso")

def filtrar_cpf(cpf, usuarios):
    usuarios_cadastrado = []
    for indice, usuario in enumerate(usuarios):
        if usuarios[indice]["cpf"] == cpf:
            usuarios_cadastrado.append(cpf)
    if len(usuarios_cadastrado) == 1:
        return "Usuário já cadastrado"
    
    if "." not in cpf or "-" not in cpf:
        return "CPF inválido"
    elif cpf[0] == "." or cpf[-1] == ".":
        return "CPF inválido"
    elif "." not in cpf[3] and "." not in cpf[7] and "-" not in cpf[11]:
       return "CPF inválido"
    elif len(cpf) < 14 or len(cpf) > 14:
        return "CPF inválido"
    else:
        return"CPF válido"

def criar_conta_nova(agencia, numero_conta, usuarios,contas):
    cpf = input("Digite o CPF (xxx.xxx.xxx-xx): ")
    conta_nova = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    if len(conta_nova) == 1:
        numero_conta = len(contas) + 1
        contas.append({"agencia": agencia, "nome": conta_nova[0]["nome"], "numero_conta": numero_conta, "cpf": cpf})
    else:
        print("Usuário não encontrado")
      

def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta["agencia"]} - Conta: {conta["numero_conta"]} - nome: {conta["nome"]} - cpf: {conta["cpf"]}")

def main():
    AGENCIA = "0001"
    numero_conta = 0
    saldo = 0
    LIMITE = 500
    numero_saques = 0
    LIMITE_SAQUES = 3
    extrato = ""
    depositos_realizados = []
    investimentos = []
    saldo_poupanca = 0
    usuarios = []
    contas = []
    menu = """
    Bem-vindo ao DIO Bank. É um prazer ter você aqui com a gente.
    Qual operação deseja realizar?
    [u] Novo Usuário
    [c] Abrir Conta
    [d] Deposito
    [s] Sacar
    [e] Extrato
    [i] Investimentos
    [p] Poupança
    [l] Listar contas
    [x] Sair 
"""
 

    while True:
        opcao = input(menu + "Opção: ").lower()
        if opcao == "u":
            if verificar("Novo usuario") == "S":
                novo_usuario(usuarios)
        elif opcao == "c":
            if verificar("Abrir contra") == "S":
                criar_conta_nova(AGENCIA, numero_conta, usuarios, contas)
        elif opcao == "d":
            if verificar("deposito") == "S":
                saldo, extrato = deposito("Deposito", saldo,extrato,depositos_realizados) 
        elif opcao == "s":
            if verificar("saque") == "S":
               saldo,extrato = saque(txt="saque",saldo=saldo,extrato=extrato,limite=LIMITE,numero_saques=numero_saques,limite_saques=LIMITE_SAQUES)
        elif opcao == "e":
            extrato = Extrato(saldo,extrato=extrato)
        elif opcao == "i":
            saldo, extrato = investimento(saldo,extrato,investimentos)
        elif opcao == "p":
            if verificar("poupança") == "S":
                saldo_poupanca, saldo, extrato = poupanca(saldo_poupanca, saldo, extrato)
        elif opcao == "l":
            listar_contas(contas)
        elif opcao == "x":
            break
        else:
            print("Operação inválida.")


main()