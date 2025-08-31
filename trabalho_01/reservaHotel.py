from datetime import datetime

class Hotel:

    reservas = []       
    numeroQuarto = 1 
    qtdQuartos = 2 # Número de quartos no hotel

    def __init__(self, nome, destino, Entrada, Saida):
        self.nome = nome
        self.destino = destino
        self.entrada = datetime.strptime(Entrada, "%d/%m/%Y")
        self.saida = datetime.strptime(Saida, "%d/%m/%Y")

        if self.verifica():
            self.reservas.append((self.nome, self.destino, self.entrada, self.saida))
            print(f"Reserva feita para {self.nome}, o numero do quarto e: {self.numeroQuarto}, estado: {self.destino}, "
                  f"de {Entrada} até {Saida}")
        else:
            print("Não há quartos disponíveis nesse período.")

    def verifica(self):
        #Verifica se há quartos disponíveis no período solicitado
        inicio = self.entrada
        fim = self.saida
        destino = self.destino
        quartosOcupados =+ 1

        for reserva in self.reservas:
            _, _, ini_reserva, fim_reserva = reserva
            # Se encontrar periodo iquala  data então quarto ocupado
            if not ((fim < ini_reserva or inicio > fim_reserva) and destino == self.destino):
                quartosOcupados =+ 1
                self.numeroQuarto =+1
                if quartosOcupados == self.qtdQuartos:
                    return False
        return True
