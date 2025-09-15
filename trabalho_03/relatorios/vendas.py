from teamplate.teamplate_method import AbstractClass

class Vendas(AbstractClass):



    def tipoRelatorio(self):
        print(" Relatorio de Vendas ")


    def calculo(self, vendas_mes):
        print(" nesse mes foram vendidos " + str(len(vendas_mes)) + " produtos")