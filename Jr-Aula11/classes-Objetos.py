class Carro:
    modelo = ""
    fabricante = ""
    motor = 0.0
    cor = ""
    portas = 0
    hibrido = False
    cambioAlt = False
    velocidade = 0

    def __init__(self, modelo, fabricante, motor, cor, portas, hibrido, cambioAlt,velocidade):
        
        self.modelo = modelo
        self.fabricante = fabricante
        self.motor = motor
        self.cor = cor
        self.portas = portas
        self.hibrido = hibrido
        self.cambioAlt = cambioAlt
        self.velocidade = velocidade


    # métodos
    def acelerar(self):
        print("Acelerando...")
        self.velocidade += 10

    def mostrarVelocidade(self):
        print(f"Você está a {self.velocidade} km/h")


gol = Carro("Gol","Wolkswagen",1.6,"vermelho",5,False,False,0)

gol.acelerar()

gol.mostrarVelocidade()

"""

Criando uma nova classe para motos:

"""




class Moto:
    cor = ""
    modelo = ""
    fabricante = ""
    ano = 0
    buzina = True
    freio = True
    velocimetro = 0

    def __init__(self, cor, modelo, fabricante,ano, buzina, freio,velocimetro):
        self.cor = cor
        self.modelo = modelo
        self.fabricante = fabricante
        self.ano = ano
        self.buzina = buzina
        self.freio = freio
        self.velocimetro = velocimetro


    def ligar(self):
        print(f"Sua {self.modelo} está ligada!")

    def acelerar(self):
        print("acelerando")
        self.velocimetro += 10
    
    def reduzir(self):
        self.velocimetro -= 10
        if(self.velocimetro >=0):
            print(f"Reduzindo velocidade\n Sua velocidade atual é : {self.velocimetro}Km/h")
    
    def velocidadeAtual(self):
        print(f"Sua velocidade atual é {self.velocimetro} km/h")
        while(True):
            question = input("Continuar acelerando ? (S/N)\n>  ").upper()
            match(question):
                case "S":
                    self.velocimetro +=10
                    print(f"Você está a {self.velocimetro} km/h")
                    continue
                case "N":
                    print(f"Velocidade atual mantida em {self.velocimetro} km/h")
                    choice = input("Deseja reduzir a velocidade atual ? (S/N)").upper()
                    if(choice =="S"):
                        self.reduzir()
                    break
                case _:
                    print("Opção Inválida - tente novamente!")
                    continue
                







mt03 = Moto("Preta", "Master Of Toque 03", "Yamaha",2018,True,True,0)


mt03.ligar()


mt03.acelerar()

mt03.velocidadeAtual()

