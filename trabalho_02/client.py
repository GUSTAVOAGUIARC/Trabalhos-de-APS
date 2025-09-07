from Factory.factoryMac import FactoryMacOs
from Factory.factoryWindows import FactoryWindows

def main():

    botao = FactoryWindows().criar_botao()
    janela = FactoryWindows().criar_janela()

   
    print(botao.teste_botao())
    print(janela.teste_janela())

    botao = FactoryMacOs().criar_botao()
    janela = FactoryMacOs().criar_janela()

    print(botao.teste_botao())
    print(janela.teste_janela())

if __name__ == "__main__":
    main()