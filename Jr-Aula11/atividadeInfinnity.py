import time
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
linha = ("------------------------------")
pularlinha = "\n"
class Fatura: 
    def __init__(self):
        self.sacola = {}
        while True:
            # self.item = input("Insira o nome do item ou digite 'sair' para parar:  ")
            # if self.item.lower() == 'sair':
            #     break
            # self.itemPrice = float(input("Insira o valor do item:  "))
            # self.qntItem = int(input("Insira a quantidade que deseja levar: "))
            
            
            # self.itens ={
            #     "Item": self.item,
            #     "Preço": self.itemPrice,
            #     "Quantidade": self.qntItem,
            # }
            
            # # self.sacola[self.item] = self.itens
            
            self.valor_totalFatura = 0
            print(linha)
            self.option = int(input("\nInforme a operação que deseja realizar \n1- Gerar fatura\n"+ "\n2- Adicionar Item\n"+"\n3- Visualizar itens\n"+"\n4- Sair\n"))
            print(linha)
            match self.option:
                case 1 :
                    self.gerar_fatura()
                case 2 :
                    self.adicionar_item()
                case 3 :
                    self.visualizar_itens()
                case 4:
                    print("Encerrando aplicação!")
                    time.sleep(1)
                    break
                case _ :
                    print("OPERACAO INVÁLIDA")


    def adicionar_item(self):
        self.item = input("Insira o nome do item:  ")
        self.itemPrice = float(input("Insira o valor do item:  "))
        self.qntItem = int(input("Insira a quantidade que deseja levar: "))
        
        
        self.itens ={
            "Item": self.item,
            "Preço": self.itemPrice,
            "Quantidade": self.qntItem,
        }
        
        self.sacola[self.item] = self.itens
        
        
    def gerar_fatura(self):
        if self.sacola.__len__() <= 0:
            print("Sacola vazia!")
            print(linha)
            time.sleep(1)
            print(pularlinha*15)
        else:
            print(f"Id -- Item ----------- Quantidade ---------- Valor Unitário\n")
            id = 0
            for x,y in self.sacola.items():
                id +=1
                print(f"{id}º | {y['Item'][0:5]} ----------- {y['Quantidade']} ---------- {y['Preço']}R$\n"
                  )

            # gerando o valor total dos itens dentro do dicionario.
            for x, y in self.sacola.items():
                quantidade = y['Quantidade']
                valorparcialItem = y['Preço']
                valorporItem = quantidade * valorparcialItem
                self.valor_totalFatura += valorporItem


            print(f"Valor total ---------- {self.valor_totalFatura:.2f}R$")


    def visualizar_itens(self):
        if self.sacola.__len__() <= 0:
            print(linha)
            print("Aqui está sua sacola:\nId--Item ------------------- Quantidade\n")
            print("__________________Sacola vazia!__________________")
            time.sleep(1)
            print(pularlinha*25)
        else:
            id = 0
            print(linha)
            print("Aqui está sua sacola:\nId--Item ------------------- Quantidade\n")
            for item,x in self.sacola.items():
                id+=1
                print(f"{id}º | {x['Item']}-------------------{x['Quantidade']}")
            print(pularlinha*10)
            print("Caso Deseje ver seus itens, role o mouse para cima ^")
            print("                                                   |")
            print(linha)
            

            
            

fatura1 = Fatura()



