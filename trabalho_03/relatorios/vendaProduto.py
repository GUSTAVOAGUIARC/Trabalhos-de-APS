from teamplate.teamplate_method import AbstractClass

class vendaProduto(AbstractClass):

    def tipoRelatorio(self):
        print(" Numero de produtos vendidos por tipo ")


    def calculo(self, vendas_mes):

        contagem = {}

        for produto, _ in vendas_mes:       # ignoramos o valor, só e necessario o tipo
            if produto in contagem:
                contagem[produto] += 1
            else:
                contagem[produto] = 1

        # Exibindo o resultado
        print("Vendas do mês por produto:")
        for produto, quantidade in contagem.items():
            print(f"{produto}: {quantidade}")