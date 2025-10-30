from Elemento import Elemento

class Obstaculo(Elemento):

    def __init__(self, nome, x, y, dano_causado):
        super().__init__(nome, x, y)
        self.dano_causado = dano_causado

