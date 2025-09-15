from relatorios.montante import montante
from relatorios.vendas import Vendas
from relatorios.vendaProduto import vendaProduto
import random

def main():

    itens = [
    ("fone_sem_fio", 500),
    ("fone_com_fio", 15),
    ("tablet", 1250),
    ("computador", 6000),
    ("celular", 5000)
]

    vendas_mes = [random.choice(itens) for i in range(random.randint(1, 10))]      # para testar estou criando  uma lista de produtos ale
                                                                                    #aleatoria com quantidade aleatoria de produtos
    mes = "Setembro"




    relatorio1 = Vendas()
    relatorio1.template_method(mes, vendas_mes)

    print("\n")

    relatorio2 = montante()
    relatorio2.template_method(mes, vendas_mes)

    print("\n")
    
    relatorio3 = vendaProduto()
    relatorio3.template_method(mes, vendas_mes)

if __name__ == "__main__":
    main()