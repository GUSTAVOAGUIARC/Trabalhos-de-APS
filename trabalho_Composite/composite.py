from typing import List
from component import Tarefa


class Composite(Tarefa):

    def __init__(self, nome: str) -> None:
        super().__init__(nome)
        self._filhos: List[Tarefa] = []

    def adicionar(self, tarefa: Tarefa) -> None:
        self._filhos.append(tarefa)
        tarefa.definir_pai(self)
        self.atualizar_conclusao()

    def remover(self, tarefa: Tarefa) -> None:
        if tarefa in self._filhos:
            self._filhos.remove(tarefa)
            tarefa.definir_pai(None)
            self.atualizar_conclusao()

    def obter_filhos(self) -> List[Tarefa]:
        return list(self._filhos)

    def concluir(self) -> None:
        for filho in self._filhos:
            filho.concluir()
        if not self._concluida:
            self._concluida = True
            self._notificar_pai()

    def desfazer(self) -> None:
        for filho in self._filhos:
            filho.desfazer()
        if self._concluida:
            self._concluida = False
            self._notificar_pai()

    def atualizar_conclusao(self) -> None:
        if self._filhos:
            todos_concluidos = all(filho.concluida for filho in self._filhos)
            if todos_concluidos and not self._concluida:
                self._concluida = True
                self._notificar_pai()
            elif not todos_concluidos and self._concluida:
                self._concluida = False
                self._notificar_pai()
