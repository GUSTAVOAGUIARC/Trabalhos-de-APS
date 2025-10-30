from Elemento import Elemento

class Unidade(Elemento):

    def __init__(self, nome, x, y, vida):
        super().__init__(nome, x, y)
        self.vida = vida

    def checar_vida(self):
        if self.vida <= 0:
            print(f"A unidade {self.nome} infelizmente veio a falecer D:")
        else:
            print(f"A vida de {self.nome} é {self.vida}")

        