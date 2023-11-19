from random import randint


class Conta:

    def __init__(self, identificador, nome, saldo):
        self.identificador = identificador
        self.nome = nome
        self.saldo = saldo

    def verificar_infor(self):
        print(f"Identificador -> {self.identificador}\n"+
              f"nome da conta -> {self.nome}\n"+
              f"saldo -> {self.saldo}\n")
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"O depósito de R$ {valor} foi realizado com sucesso")


class Conta_corrente(Conta):
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo-=valor
            print("Saque realizado com sucesso!")
        else:
            print(f"""Saldo insuficiente!\n
                Saldo em conta -> {self.saldo}
            """)
            

class Conta_poupanca(Conta):
    def __init__(self, identificador, nome, saldo, juros):
        super().__init__(identificador, nome, saldo)
        self.juros = juros 

        # polimorfismo
    def verificar_infor(self):
        super().verificar_infor()
        print(f"Juros -> {self.juros}")



while True:
    escolha = int(input("1- Conta Corrente\n"
    "2- Conta Poupança\n"
    "0- Finalizar Sistema\n"))


    match escolha:
        case 1 :
            identificador = randint(0, 1000)
            nome = input("Digite o nome do proprietário da conta:\n ")
            saldo = float(input("Informe o saldo inicial da conta:\n "))

            conta = Conta_corrente(identificador, nome, saldo)

            while True:
                escolha = int(input("Digite uma das opções:\n"
                                    "1 - Verificar informaçoes\n"
                                    "2 - Depositar\n"
                                    "3 - Sacar\n"
                                    "0 - Sair da conta\n"
                                    ))
                match escolha:
                    case 1:
                        conta.verificar_infor()
                    case 2:
                        valor = float(input("Digite o valor a ser depositado:\n"))
                        
                        conta.depositar(valor)
                    case 3:
                        valor = float(input("Digite o valor a ser sacar:\n"))
                        
                        conta.sacar(valor)
                    case 0:
                        break
                    case _:
                        print("Escolha Inválida.")

        case 2:
                indetificador = randint(0, 10000)
                nome = input("Digite o nome da conta: ")
                saldo = float(input("Digite o saldo inicial da conta: "))
                juros = float(input("Digite o valor de juros da conta: "))

                conta = Conta_poupanca(indetificador, nome, saldo, juros)

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
