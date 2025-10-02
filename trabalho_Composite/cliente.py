from composite import Composite
from leaf import Sub_Tarefa


def main():
    cardapio = Composite('Cardápio')

    # Categorias principais
    bebidas = Composite('Bebidas')
    pratos = Composite('Pratos')
    sobremesas = Composite('Sobremesas')

    cardapio.adicionar(bebidas)
    cardapio.adicionar(pratos)
    cardapio.adicionar(sobremesas)

    # Bebidas
    bebidas.adicionar(Sub_Tarefa('Coca-Cola'))
    bebidas.adicionar(Sub_Tarefa('Suco de Laranja'))

    # Pratos
    pratos.adicionar(Sub_Tarefa('Pizza'))
    pratos.adicionar(Sub_Tarefa('Lasanha'))

    # Sobremesas
    sobremesas.adicionar(Sub_Tarefa('Pudim'))
    sobremesas.adicionar(Sub_Tarefa('Sorvete'))

    # Imprimir estado inicial
    print('\n ESTADO INICIAL DO CARDÁPIO:')
    print(cardapio.imprimir_arvore())

    # Concluir Subtarefas
    print('\n CONCLUINDO SUBTAREFAS:')
    Sub_Tarefa('Coca-Cola').concluir()
    Sub_Tarefa('Lasanha').concluir()
    Sub_Tarefa('Pizza').concluir()
    print(cardapio.imprimir_arvore())

    # concluir tarefas
    print('\n CONCLUINDO TAREFAS:')
    sobremesas.concluir()
    print(cardapio.imprimir_arvore())

    # desfazer conclusão
    print('\n DESFAZENDO CONCLUSÕES:')
    Sub_Tarefa('Pizza').desfazer()
    print(cardapio.imprimir_arvore())

    print('\n DESFAZENDO todas as conclusões:')
    cardapio.desfazer()
    print(cardapio.imprimir_arvore())


if __name__ == "__main__":
    main()
