import copy
from Elemento import Elemento
from Memento import Memento

class Mapa:

    def __init__(self):
        self.elementos = [] #lista de elementos do mapa

    def adicionar_elemento(self, elemento):
        if isinstance(elemento, Elemento):  # garante que é uma subclasse
            self.elementos.append(elemento)
        else:
            raise TypeError("Isso não é um Elemento.")
    
    def remover_elemento(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)
    
     # Cria um novo Memento usando o Prototype
    def salvar_estado(self):
        estado_clone = copy.deepcopy(self.elementos)
        return Memento(estado_clone)
    
    # Restaura a partir de um Memento
    def restaurar_estado(self, memento):
        self.elementos = copy.deepcopy(memento.get_estado())

    def listar_elementos(self):
        if not self.elementos:
            print("O mapa está vazio.")
        else:
            print("Elementos no mapa:")
            for elemento in self.elementos:
                print(f" - {elemento}")