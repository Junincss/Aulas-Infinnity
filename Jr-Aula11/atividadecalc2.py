class Calculadora:
    def __init__(self):
        while True:
            self.num1 = float(input("Digite o primeiro valor: "))
            self.num2 = float(input("Digite o segundo valor: "))

            self.operacao = int(input("Digite a operação: \n1 - Somar \n2 - Subtrair \n3 - Multiplicar \n4 - Dividir"))

            match self.operacao:
                case 1:
                    self.soma()
                case 2:
                    self.subtracao()
                case 3:
                    self.multiplicacao()
                case 4:
                    self.divisao()
                case 5:
                    break
                case _:
                    print("Operação inválida")
    def soma(self):
        print(self.num1 + self.num2)

    def subtracao(self):
        print(self.num1 - self.num2)

    def multiplicacao(self):
        print(self.num1 * self.num2)
    
    def divisao(self):
        print(self.num1 / self.num2)

calc = Calculadora()