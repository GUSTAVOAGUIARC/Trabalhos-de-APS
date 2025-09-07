# AbstractFactory.py
from abc import ABC, abstractmethod

class AbstractFactory(ABC):

    @abstractmethod
    def criar_botao(self):
        pass

    @abstractmethod
    def criar_janela(self):
        pass
