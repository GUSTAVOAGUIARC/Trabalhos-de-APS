from composite import Composite
from leaf import Sub_Tarefa


def main():
    #nivel 1
    cardapio = Composite('Cardápio')

    # Categorias principais  nivel 2
    bebidas = Composite('Bebidas')
    pratos = Composite('Pratos')
    sobremesas = Composite('Sobremesas')

    cardapio.adicionar(bebidas)
    cardapio.adicionar(pratos)
    cardapio.adicionar(sobremesas)

    # Bebidas  nivel 3
    refrigerantes = Composite('Refrigerantes')
    sucos = Composite('Sucos')
    bebidas.adicionar(refrigerantes)
    bebidas.adicionar(sucos)
    
    # bebidas nivel 4
    coca = Sub_Tarefa('Coca-Cola')
    guarana = Sub_Tarefa('Guaraná')
    suco_laranja = Sub_Tarefa('Suco de Laranja')
    suco_uva = Sub_Tarefa('Suco uva')

    refrigerantes.adicionar(coca)
    refrigerantes.adicionar(guarana)
    sucos.adicionar(suco_laranja)
    sucos.adicionar(suco_uva)

    # Pratos nivel 3
    pizza = Sub_Tarefa('Pizza')
    lasanha = Sub_Tarefa('Lasanha')
    espaguete = Sub_Tarefa('Espaguete')
    risoto = Sub_Tarefa('Risoto')
    salada = Sub_Tarefa('Salada')
    carne = Sub_Tarefa('Carne')

    pratos.adicionar(pizza)
    pratos.adicionar(lasanha)
    pratos.adicionar(espaguete)
    pratos.adicionar(risoto)
    pratos.adicionar(salada)
    pratos.adicionar(carne)

    # Sobremesas nivel 3
    doces = Composite('Doces')
    sobremesas.adicionar(doces)

    pudim = Sub_Tarefa('Pudim')
    sorvete = Sub_Tarefa('Sorvete')
    doces.adicionar(pudim)
    doces.adicionar(sorvete)

    # Imprimir estado inicial
    print('\n ESTADO INICIAL DO CARDÁPIO:')
    print(cardapio.imprimir_arvore())

    # Concluir Subtarefas
    print('\n CONCLUINDO SUBTAREFAS:')
    coca.concluir()
    lasanha.concluir()
    pizza.concluir()
    suco_laranja.concluir()
    print(cardapio.imprimir_arvore())

    # concluir tarefas
    print('\n CONCLUINDO TAREFAS:')
    refrigerantes.concluir()
    print(cardapio.imprimir_arvore())

    # desfazer conclusão
    print('\n DESFAZENDO CONCLUSÕES:')
    pizza.desfazer()
    print(cardapio.imprimir_arvore())

    print('\n DESFAZENDO todas as conclusões:')
    cardapio.desfazer()
    print(cardapio.imprimir_arvore())


if __name__ == "__main__":
    main()
