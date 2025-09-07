from .abstractFactory import AbstractFactory
from Object.botaoMac import BotaoMac
from Object.janelaMac import JanelaMac

class FactoryMacOs(AbstractFactory):
    def criar_botao(self):
        return BotaoMac()

    def criar_janela(self):
        return JanelaMac()