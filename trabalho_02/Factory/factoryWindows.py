from .abstractFactory import AbstractFactory
from Object.botaoWindows import BotaoWindows
from Object.janelaWindows import JanelaWindows

class FactoryWindows(AbstractFactory):
    def criar_botao(self):
        return BotaoWindows()

    def criar_janela(self):
        return JanelaWindows()