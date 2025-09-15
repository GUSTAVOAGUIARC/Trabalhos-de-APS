from teamplate.teamplate_method import AbstractClass

class montante(AbstractClass):



    def tipoRelatorio(self):
        print(" Relatorio de lucro da empresa ")


    def calculo(self, vendas_mes):
        lucro = 0
        for i in range(len(vendas_mes)):
            lucro += vendas_mes[i][1]

        print(" O Lucro total da empresa foi de :" + str(lucro))

