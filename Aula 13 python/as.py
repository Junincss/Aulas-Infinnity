from random import randint

class Conta:
    def __init__(self, indetificador, nome, saldo):
        self.indetificador = indetificador
        self.nome = nome
        self.saldo = saldo
    
    def verificar_infor(self):
        print(f"indetificador -> {self.indetificador}\n"
              f"nome da conta -> {self.nome}\n"
              f"saldo -> {self.saldo}\n")
    
    def deposito(self, valor):
        self.saldo += valor

        print("O Deposito foi realizado com sucesso")

class Conta_corrente(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print("Valor insuficiente.")
        else:
            self.saldo -= valor

            print("Saque efetuado com sucesso")

class Conta_poupança(Conta):
    def __init__(self, indetificador, nome, saldo, juros):
        super().__init__(indetificador, nome, saldo)
        self.juros = juros

while True:
    escolha = int(input("Digite uma das escolhas abaixo:\n"
                        "1 - Conta Corrente\n"
                        "2 - Conta Poupança\n"
                        "0 - Finalizar Sistema\n"))
    
    match escolha:
        case 1:
            # indetificador = int(input("Digite o indetificador da conta: "))
            indetificador = randint(0, 10000)
            nome = input("Digite o nome da conta: ")
            saldo = float(input("Digite o saldo inicial da conta: "))

            conta = Conta_corrente(indetificador, nome, saldo)

            while True:
                escolha = int(input("Digite uma das opções:\n"
                                    "1 - Verificar informações\n"
                                    "2 - Depositar\n"
                                    "3 - Sacar\n"
                                    "0 - sair da conta\n"))
                
                match escolha:
                    case 1:
                        conta.verificar_infor()
                    
                    case 2:
                        valor = float(input("Digite o valor a ser depositado: "))

                        conta.deposito(valor)
                    
                    case 3:
                        valor = float(input("Digite o valor a ser sacado: "))

                        conta.sacar(valor)
                    
                    case 0:
                        break

                    case _:
                        print("Escolha inexistente")

        case 2:
            indetificador = randint(0, 10000)
            nome = input("Digite o nome da conta: ")
            saldo = float(input("Digite o saldo inicial da conta: "))
            juros = float(input("Digite o valor de juros da conta: "))

            conta = Conta_poupança(indetificador, nome, saldo, juros)

            while True:
                escolha = int(input("Digite uma das opções:\n"
                                    "1 - Verificar informações\n"
                                    "2 - Depositar\n"
                                    "0 - sair da conta\n"))
                
                match escolha:
                    case 1:
                        conta.verificar_infor()
                    
                    case 2:
                        valor = float(input("Digite o valor a ser depositado: "))

                        conta.deposito(valor)
                    
                    case 0:
                        break

                    case _:
                        print("Escolha inexistente")

        case 0:
            break

        case _:
            print("Opções inexistente.")