import copy

class Elemento:

    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y


    def clonar(self):
        return copy.deepcopy(self) # Cria uma nova cópia do Elemento
    

    def __repr__(self): # Formata o print do Elemento
        return f"{self.__class__.__name__}({self.nome}, x={self.x}, y={self.y})"

    