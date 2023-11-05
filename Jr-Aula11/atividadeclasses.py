"""
Crie uma classe chamada Calculadora que tenha como atributos dois valores e os seguintes métodos:
    - Soma
    - Subtração
    - Multiplicação
    - Divisão

"""


class Calculator:

    def __init__(self, value1, value2, result):
        self.value1 = value1
        self.value2 = value2
        self.result = result
    
    def sum(self):
        self.result = self.value1 + self.value2
        print(f"A soma dos valores {self.value1} + {self.value2} = {self.result} \n ")

    def subtract(self):
        self.result = self.value1 - self.value2
        print(f"O resultado da subtração dos valores {self.value1} - {self.value2} = {self.result} \n ")

    def multiply(self):
        self.result = self.value1 * self.value2
        print(f"A multiplição de {self.value1} * {self.value2} = {self.result} \n ")

    def toDivide(self):
        self.result = self.value1 / self.value2
        print(f"O resultado da divisão dos valores {self.value1} / {self.value2} = {self.result} \n ")


value1 = int(input("Digite o primeiro valor: "))
value2 = int(input("Digite o segundo valor: "))


calc = Calculator(value1,value2,0)

calc.sum()
calc.subtract()
calc.multiply()
calc.toDivide()