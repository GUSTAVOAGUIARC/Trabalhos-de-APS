from Elemento import Elemento

class Terreno(Elemento):

    def __init__(self, nome, x, y, formato):
        super().__init__(nome, x, y)
        self.formato = formato