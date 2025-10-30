class Memento:
    def __init__(self, estado_mapa):
        self._estado_mapa = estado_mapa

    def get_estado(self):
        return self._estado_mapa