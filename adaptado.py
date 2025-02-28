from datetime import datetime

class PessoaFisica:
    def __init__(self, nome, cpf, data_nasc):
        self._nome = nome
        self._cpf = cpf
        self._data_nasc = data_nasc


class Cliente(PessoaFisica):
    _clientes = []

    def __init__(self, nome, cpf, data_nasc, endereco):
        super().__init__(nome, cpf, data_nasc)
        self._endereco = endereco
        self._contas = []

    def adicionar_cliente(self):
        self._clientes.append(cliente)

    @classmethod
    def listar_clientes(cls):
        for cliente in cls._clientes:
            print(f"Nome: {cliente._nome}, CPF: {cliente._cpf}, Data de Nascimento: {cliente._data_nasc}, Endereço: {cliente._endereco}")

    @classmethod
    def buscar_cliente_pelo_cpf(cls, cpf):
        cliente = next((cliente for cliente in cls._clientes if cliente._cpf == cpf), None)
        
        return cliente


class Conta:
    _contas = []

    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = []

    def adicionar_conta(self):
        self._contas.append(conta)

    @classmethod
    def listar_contas(cls):
        for conta in cls._contas:
            print(f"Cliente: {conta._cliente._nome}, Agência: {conta._agencia}, Número: {conta._numero}, Saldo: R$ {conta._saldo}")

    @classmethod
    def buscar_conta_pelo_numero(cls):
        numero = int(input("Informe o número da conta: "))

        for conta in cls._contas:
            return next((conta for conta in cls._contas if conta._numero == numero), None)
        
        return None

    def depositar(self, valor):
        self._saldo += valor
        print("Depósito de R$ {valor} realizado com sucesso.")

        historico = Historico(f"Depósito: R$ {valor:.2f}, {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        historico.adicionar_transacao(conta)

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso")
            
            historico = Historico(f"Saque: R$ {valor:.2f}, {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            historico.adicionar_transacao(self)
        else:
            print(f"Valor de saque acima do saldo atual. Saldo atual: R$ {self._saldo}")

    def exibir_saldo(self):
        print(f"Saldo: R$ {self._saldo}")

    def exibir_historico(self):
        print("===== Histórico =====")
        
        for transacao in self._historico:
            print(transacao)

        print(f"Saldo: R$ {self._saldo}")
        print("=====================")

    
class Historico:
    def __init__(self, transacao):
        self._transacao = transacao
    
    def adicionar_transacao(self, conta):
        conta._historico.append(self._transacao)


while True:
    print('''
          Menu:
          1 - Cadastrar cliente
          2 - Listar clientes
          3 - Criar conta
          4 - Listar contas
          5 - Depositar
          6 - Sacar
          7 - Consultar saldo
          8 - Consultar histórico
          0 - Sair
    ''')
    opcao = input("Selecione uma operação: ")

    if opcao == '1': # Cadastrar cliente
        nome = input("Informe o nome: ")
        cpf = input("Informe o CPF: ")
        data_nasc = input("Informe a data de nascimento: ")
        endereco = input("Informe o endereço: ")

        cliente = Cliente(nome, cpf, data_nasc, endereco)

        cliente.adicionar_cliente()

    elif opcao == '2': # Listar clientes
        Cliente.listar_clientes()

    elif opcao == '3': # Criar conta
        cpf = input("Informe o CPF: ")
        cliente = Cliente.buscar_cliente_pelo_cpf(cpf)
        
        if cliente:
            conta = Conta(len(Conta._contas) + 1, cliente)
            conta.adicionar_conta()
            print("Conta criada com sucesso.")
        else:
            print("CPF não encontrado.")

    elif opcao == '4': # Listar contas
        Conta.listar_contas()

    elif opcao == '5': # Depositar
        conta = Conta.buscar_conta_pelo_numero()
        if conta:
            valor = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)
            
        else:
            print("Número da conta não encontrada.")

    elif opcao == '6': # Sacar
        conta = Conta.buscar_conta_pelo_numero()
        if conta:
            valor = float(input("Informe o valor do saque: "))
            conta.sacar(valor)

        else:
            print("Número da conta não encontrada.")

    elif opcao == '7': # Consultar saldo
        conta = Conta.buscar_conta_pelo_numero()
        if conta:
            conta.exibir_saldo()
        else:
            print("Número da conta não encontrada.")

    elif opcao == '8': # Consultar histórico
        conta = Conta.buscar_conta_pelo_numero()
        if conta:
            conta.exibir_historico()
        else:
            print("Número da conta não encontrada.")

    elif opcao == '0':
        print("Saindo")
        break

    else:
        print("Opção inválida.")