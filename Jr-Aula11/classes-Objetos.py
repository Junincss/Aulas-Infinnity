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






