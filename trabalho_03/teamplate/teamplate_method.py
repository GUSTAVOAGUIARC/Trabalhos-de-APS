from abc import ABC, abstractmethod
import datetime

class AbstractClass(ABC):

    def template_method(self, mes, vendas_mes):
        self.formatar()
        self.nomeEmpresa()
        self.tipoRelatorio()
        self.data()
        self.dataRelatorio(mes)
        self.dados(vendas_mes)
        self.calculo(vendas_mes)

        
    
    def nomeEmpresa(self):
        print("Uma empresa qualquer LTDA")

    def data(self):
        print(" Relatorio Gerado no dia" + datetime.datetime.now().strftime("%d/%m/%Y"))


    def dataRelatorio(self, mes):
        print(" Relatorio corespondente ao mes " + mes)


    def dados(self, vendas_mes):
        print(" Dados do relatorio:")
        for i in range(len(vendas_mes)):
            print(f" Produto: {vendas_mes[i][0]} - Preco: {vendas_mes[i][1]}")
        print("\n")

    def formatar(self):
        print("===========================================================")

    @abstractmethod                   # devera ser implementado nas classes concretas
    def calculo(self, vendas_mes):
        pass

    @abstractmethod
    def tipoRelatorio(self):
        pass
