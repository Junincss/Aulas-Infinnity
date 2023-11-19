class Eevee:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel
        self.tipo = "Normal"

    def ataque_basico(self):
        print(F"{self.nome} Usou investida!")

class Vaporeon(Eevee):
    def __init__(self, nome, nivel):
        super().__init__(nome, nivel)
        self.tipo = "Água"

    def ataque_basico(self):
        print(f"{self.nome} Usou Jato d'água!")


pokemon = Vaporeon("chico",10)

pokemon.ataque_basico()