from typing import List
from time import sleep
from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []
def main() -> None:
    menu()

def menu() -> None:
    print('================================================')
    print('=============== Bem vindo ======================')
    print('============= Beto86 BANCK =====================')
    print('================================================')

    print('Selecione uma opcao')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar deposito')
    print('4 - Efetuar transferencia')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao: int = int(input())
    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_tranferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print("Volte Senpre!!")
        sleep(3)
        exit(0)
    else:
        print('Opcao Invalida!')
        sleep(2)
        menu()
    
def criar_conta() -> None:
    print('================================================')
    print('============= Criar cliente ================')
    print('================================================')

    nome: str = input("Informe o nome do cliente: ")
    email: str = input("Informe o email do cliente: ")
    cpf: str = input("Informe o cpf do cliente: ")
    data_nascimento: str = input("Informe a data de nascimento do cliente: ")
    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)
    contas.append(conta)
    print('Conta criada com sucesso.')
    print('Dados da conta: ')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(conta)
    sleep(3)
    menu()

def efetuar_saque() -> None:
    if len(contas) > 0:
        print('================================================')
        print('============= SAQUE ============================')
        print('================================================')
        numero: int = int(input("Informe o numero da conta: "))
        conta: Conta = buscar_contas_por_numero(numero)
        if conta:
            valor: float = float(input("Informe o valor para saque: "))
            conta.sacar(valor)
        else:
            print(f"Nao foi encontrada a conta com numero {numero}")
    else:
        print('Ainda nao existem contas cadastradas')
    sleep(3)
    menu()

def efetuar_deposito() -> None:
    if len(contas) > 0:
        print('================================================')
        print('============= DEPOSITO =========================')
        print('================================================')
        numero: int = int(input("Informe o numero da conta: "))
        conta: Conta = buscar_contas_por_numero(numero)
        if conta:
            valor: float = float(input("Informe o valor para deposito: "))
            conta.depositar(valor)
        else:
            print(f"Nao foi encontrada a conta com numero {numero}")
    else:
        print('Ainda nao existem contas cadastradas')
    sleep(3)
    menu()

def efetuar_tranferencia() -> None:
    if len(contas) > 0:
        print('================================================')
        print('============= TRANSFERENCIA ====================')
        print('================================================')
        numero_o: int = int(input("Informe o numero da conta: "))
        conta_o: Conta = buscar_contas_por_numero(numero_o)
        if conta_o:
            numero_d: int = int(input("Informe o numero da conta de destino: "))
            conta_d: Conta = buscar_contas_por_numero(numero_d)
            if conta_d:
                valor: float = float(input("Informe o valor para transferencia: "))
                conta_o.transferir(conta_d, valor)
            else:
                print(f"A conta com numero {numero_d} nao foi encontrado")
        else:
            print(f"Nao foi encontrada a conta com numero {numero_o}")
    else:
        print('Ainda nao existem contas cadastradas')
    sleep(3)
    menu()

def listar_contas() -> None:
    if len(contas) > 0:
        print('================================================')
        print('============= Listar Contas ===================')
        print('================================================')
        for conta in contas:
            print(conta)
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
    else: 
        print('Ainda nao tem contas cadastradas!')
    sleep(3)
    menu()

def buscar_contas_por_numero(numero: int) -> Conta:
    c: Conta = None
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c

    
if __name__ == '__main__':
    main()
