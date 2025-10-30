class Caretaker:

    def __init__(self, mapa):
        self.mapa = mapa
        self._historico = []
        self._indice_atual = -1


    def salvar(self): # Remove estados à frente (caso seja feito um undo e depois algo diferente)
        self._historico = self._historico[:self._indice_atual + 1]
        self._historico.append(self.mapa.salvar_estado())
        self._indice_atual += 1


    def desfazer(self):
        if self._indice_atual > 0:
            self._indice_atual -= 1
            self.mapa.restaurar_estado(self._historico[self._indice_atual])
        else:
            print("Nada para desfazer.")


    def refazer(self):
        if self._indice_atual < len(self._historico) - 1:
            self._indice_atual += 1
            self.mapa.restaurar_estado(self._historico[self._indice_atual])
        else:
            print("Nada para refazer.")