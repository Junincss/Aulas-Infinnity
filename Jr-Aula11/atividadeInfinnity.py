"""
Crie uma classe chamada Fatura que possa ser utilizada por uma loja de
suprimentos de informática para representar uma fatura de um item
vendido na loja. Uma fatura deve incluir as seguintes informações como
atributos:

    - O nome do item;
    - O preço unitário do item;
    - A Quantidade de item a ser faturada;
    - Valor total da fatura;

Sua classe deve ter um construtor que inicialize todos os atributos menos o
valor total da fatura. Além disso, forneça um método chamado
gerar_fatura que calcula o valor da fatura (isto é, multiplicar a quantidade
pelo preço por item).

"""

class Fatura: 
    def __init__(self):
        while True:
            self.item = input("Insira o nome do item:  ")
            self.itemPrice = float(input("Insira o valor do item:  "))
            self.qntItem = int(input("Insira a quantidade que deseja levar: "))
            self.valor_totalFatura = 0
            self.option = int(input("Informe a operação que deseja realizar \n1- Gerar fatura\n"+"\n--------------------------\n"))
            match self.option:
                case 1 :
                    self.gerar_fatura()
                case _ :
                    print("OPERACAO INVÁLIDA")



    def gerar_fatura(self):
        print(f"Item    ----------- Quantidade\n"+
              f"{self.item[0:4]}... -----x----- {self.qntItem}\n\n\n"+
              f"Valor total ---------- {self.qntItem*self.itemPrice:.2f}R$"
              )

fatura1 = Fatura()


"""
insira métodos para acrescentar o produto a fatura e depois gerá-la 


"""


