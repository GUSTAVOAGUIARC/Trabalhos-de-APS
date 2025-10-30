from Elemento import Elemento


class Construcao(Elemento):

    def __init__(self, nome, x, y, altura):
        super().__init__(nome, x, y)
        self.altura = altura
