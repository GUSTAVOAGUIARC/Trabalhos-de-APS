from __future__ import annotations   # permite referenciar uma classe que ainda não foi definida (não é necessário em versões mais novas do Python)
from abc import ABC, abstractmethod
from typing import Optional


class Tarefa(ABC):
    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.pai: Optional[Tarefa] = None
        self._concluida: bool = False

    def definir_pai(self, pai: Optional[Tarefa]) -> None:
        self.pai = pai

    @property                                           # o property permite acessar o método como se fosse um atributo
    def concluida(self) -> bool:
        return self._concluida

    @abstractmethod
    def concluir(self) -> None:
        pass

    @abstractmethod
    def desfazer(self) -> None:
        pass
    
    @abstractmethod
    def obter_filhos(self):
        pass

    def imprimir_arvore(self, identacao: str = "") -> str:
        status = "[CONCLUÍDA]" if self.concluida else "[NÃO CONCLUÍDA]"
        s = f"{identacao}- {self.nome} {status}\n"
        for filho in self.obter_filhos():
            s += filho.imprimir_arvore(identacao + "    ")
        return s

    
    def _notificar_pai(self) -> None:
        if self.pai is not None:
            self.pai.atualizar_conclusao()
