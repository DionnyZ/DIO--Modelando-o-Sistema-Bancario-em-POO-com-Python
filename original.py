import textwrap

class PessoaFisica:
    def __init__(self, cpf, nome, data_nasc):
        self._cpf = cpf
        self._nome = nome
        self._data_nasc = data_nasc

class Cliente(PessoaFisica):
    def __init__(self, cpf, nome, data_nasc, endereco):
        super().__init__(cpf, nome, data_nasc)
        self._endereco = endereco
        self._contas = []
    
    def realizar_transacao(self, conta, transacao):
        if transacao == 'sacar':
            valor = input('Informe o valor a ser sacado: ')
            Conta.sacar(valor)
        else:
            pass

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def exibir_dados(self):
        for conta in self._contas:
            linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))
        return self._cpf, self._nome, self._data_nasc, self._endereco
    
    def buscar_cliente_pelo_cpf(self, cpf):
        usuarios_filtrados = [cliente for cliente in self._clientes if cliente["cpf"] == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None

class Conta:
    def __init__(self, saldo, numero, cliente):
        self._saldo = saldo
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = []
        self._numero_saques = 0

    def saldo(self):
        pass

    def nova_conta(self, cliente, clientes):
        self._contas.append({"agencia": cliente._agencia, "numero_conta": len(self._contas) + 1, "cliente": cliente})

    def sacar(self, valor):
        excedeu_saldo = valor > self._saldo
        excedeu_limite = valor > ContaCorrente.get_limite()
        excedeu_saques = self._numero_saques >= ContaCorrente.get_limite_saques()

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            return False

        elif excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            return False

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return False

        elif valor > 0:
            self.saldo -= valor
            self._historico += f"Saque:\t\tR$ {valor:.2f}\n"
            self._numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

class ContaCorrente(Conta):
    def __init__(self):
        self._limite = 500
        self._limite_saques = 3
    
    def get_limite(self):
        return self._limite
    
    def get_limite_saques(self):
        return self._limite_saques

class Historico:
    def adicionar_transacao(self, transacao):
        self._transacao += transacao

class Transacao(Historico):
    def registrar(self, conta):
        super().adicionar_transacao()

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor