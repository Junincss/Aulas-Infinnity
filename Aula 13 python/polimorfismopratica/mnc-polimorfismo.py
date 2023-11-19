from abc import ABC, abstractmethod

"""
Faça um programa que contenha 3 classes: Carro,
barco e avião, eles possuem 3 atributos:
Nome_do_veiculo, Quantidade_de_motores e
tem_rodas, e um método chamado buzinar, o
método buzinar da classe carro deve retornar

"Biiiii"
,

da classe barco:

"Foooom
"
e avião:

"Tem buzina?"

Crie uma instância para cada classe e imprime na
tela todas as informações de cada um.

Lembre-se de utilizar Superclasses e Polimorfismo

"""



class Veiculo(ABC):
    def __init__(self,Nome_do_veiculo,Quantidade_de_motores,tem_rodas):
        self.__Nome_do_veiculo = Nome_do_veiculo #propriedade encapsulada.
        self.Quantidade_de_motores = Quantidade_de_motores
        self.tem_rodas = tem_rodas


    # encapsulamento somente para mostrar 
    @property
    def Nome_do_veiculo(self):
        return self.__Nome_do_veiculo

    @Nome_do_veiculo.setter
    def Nome_do_veiculo(self):
      self.__Nome_do_veiculo = self.__Nome_do_veiculo


    @abstractmethod
    def buzinar (self):
        pass

    def apresentar(self):
        print(f"Nome do veículo: {self.__Nome_do_veiculo}\n"
              f"Quantidade de motores: {self.Quantidade_de_motores}\n"
              f"Tem rodas? : {self.tem_rodas}\n")


class Car(Veiculo):
    def buzinar(self):
        print(f"Biiiii")
        

class Barco(Veiculo):

    def buzinar(self):
        print(f"Foooom")

class Aviao(Veiculo):

    def buzinar(self):
        print(f"Tem buzina?")
        
carro = Car("Celta",1,True)
navio = Barco('Titanic',2,True)
aviao = Aviao("arroz", 2, True)

print(carro.Nome_do_veiculo)

carro.__Nome_do_veiculo = "Rengade"
print(carro.Nome_do_veiculo)

# carro.apresentar()
# carro.buzinar()
# navio.apresentar()
# navio.buzinar()
# aviao.apresentar()
# aviao.buzinar()