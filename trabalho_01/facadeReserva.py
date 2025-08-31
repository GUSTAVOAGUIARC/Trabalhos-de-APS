# facadeReserva.py

from reservaPassagem import Passagem
from reservaHotel import Hotel
from reservaCarro import Carro

class FacadeReserva:
    def __init__(self, cliente):
        
        self.nome = cliente['nome']
        self.origem = cliente['origem']
        self.destino = cliente['destino']
        self.diaIda = cliente['diaIda']
        self.diaVolta = cliente['diaVolta']

    def reservarTudo(self):
        # Reservar passagem
        print("\n")
        Passagem(self.nome, self.origem, self.destino, self.diaIda, self.diaVolta)
        Carro(self.nome,self.destino, self.diaIda, self.diaVolta)
        Hotel(self.nome,self.destino, self.diaIda, self.diaVolta)
    
    def reservarCarro(self):
        print("\n")
        Carro(self.nome,self.destino, self.diaIda, self.diaVolta)
    
    def reservarPassagem(self):
        print("\n")
        Passagem(self.nome, self.origem, self.destino, self.diaIda, self.diaVolta)
    
    def reservarHotel(self):
        print("\n")
        Hotel(self.nome,self.destino, self.diaIda, self.diaVolta)