from component import Tarefa

class Sub_Tarefa(Tarefa):

    def concluir(self) -> None:
        if not self._concluida:
            self._concluida = True
            self._notificar_pai()

    def desfazer(self) -> None:
        if self._concluida:
            self._concluida = False
            self._notificar_pai()

    # Folhas não têm filhos, retorna lista vazia
    def obter_filhos(self):
        return []