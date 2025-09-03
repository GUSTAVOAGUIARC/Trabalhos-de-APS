from datetime import datetime

class Carro:

    agendaPassagem = []
    qtdCarros = 2       #Numeros de carros que podem ser alugados em um local especifico

    def __init__(self,nome, destino, diaIda, diaVolta):
        self.nome = nome
        self.destino = destino
        self.inicioAluguel = datetime.strptime(diaIda, "%d/%m/%Y")          #convertendo o formato da data
        self.fimAluguel = datetime.strptime(diaVolta, "%d/%m/%Y")

        if self.verifica():

            self.agendaPassagem.append((self.nome, self.inicioAluguel, self.fimAluguel , self.destino))
            print(f"Carro reservado no nome de: {self.nome}, do dia: {diaIda} até {diaVolta}")

        else:
            raise ValueError("Carro não disponível nesse período")

    def verifica(self):
        inicio = self.inicioAluguel
        fim = self.fimAluguel
        carrosEncontrados = 0

        for reserva in self.agendaPassagem:
            _, inicio_reserva, fim_reserva, destino = reserva
            if ( not(fim < inicio_reserva or inicio > fim_reserva) and self.destino == destino):
                carrosEncontrados += 1
                if carrosEncontrados == self.qtdCarros:
                    return False
        return True