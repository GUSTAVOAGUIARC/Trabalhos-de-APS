from Mapa import Mapa
from Caretaker import Caretaker
from Terreno import Terreno
from Unidade import Unidade
from Obstaculo import Obstaculo
from Construcao import Construcao


# Criação do mapa e do caretaker
mapa = Mapa()
caretaker = Caretaker(mapa)

# Adiciona um terreno e salva o estado
t1 = Terreno("Campo Verde", 10, 20, "retangular")
mapa.adicionar_elemento(t1)
caretaker.salvar()
print("\n[1] Terreno adicionado:")
mapa.listar_elementos()

# Adiciona uma unidade e salva o estado
u1 = Unidade("Soldado", 5, 8, 100)
mapa.adicionar_elemento(u1)
caretaker.salvar()
print("\n[2] Unidade adicionada:")
mapa.listar_elementos()

# Adiciona um obstáculo e salva o estado
o1 = Obstaculo("Pedregulho com espinhos", 7, 9, 10)
mapa.adicionar_elemento(o1)
caretaker.salvar()
print("\n[3] Obstáculo adicionado:")
mapa.listar_elementos()

# Desfaz última ação (remove o obstáculo)
caretaker.desfazer()
print("\n[4] Desfazer:")
mapa.listar_elementos()

# Refaz (adiciona o mesmo obstáculo novamente)
caretaker.refazer()
print("\n[5] Refazer:")
mapa.listar_elementos()

# Adiciona uma construção e salva o estado
c1 = Construcao("Torre de Vigia", 12, 14, 30)
mapa.adicionar_elemento(c1)
caretaker.salvar()
print("\n[6] Construção adicionada:")
mapa.listar_elementos()

# Testa mais um desfazer
caretaker.desfazer()
print("\n[7] Desfazer novamente:")
mapa.listar_elementos()