from datetime import datetime

class Hotel:

    reservas = []       
    numeroQuarto = 1 # não mudar!! mostra o numero do quarto no print
    qtdQuartos = 2 # Número de quartos no hotel

    def __init__(self, nome, destino, Entrada, Saida):
        self.nome = nome
        self.destino = destino
        self.entrada = datetime.strptime(Entrada, "%d/%m/%Y")
        self.saida = datetime.strptime(Saida, "%d/%m/%Y")

        if self.verifica():
            self.reservas.append((self.nome, self.destino, self.entrada, self.saida))
            print(f"Reserva feita para {self.nome}, o numero do quarto e: {self.numeroQuarto}, Pais: {self.destino}, "
                  f"de {Entrada} até {Saida}")
        else:
            raise ValueError("Não a quartos disponives nesse periodo")

    def verifica(self):
        #Verifica se há quartos disponíveis no período solicitado
        inicio = self.entrada
        fim = self.saida
        quartosOcupados = 0

        for reserva in self.reservas:
            _, destino, inicio_reserva, fim_reserva = reserva         # retirar informação da reserva
            # Se encontrar nas reservas uma reserva que de comflito com o horario pedido
            if  (not(fim < inicio_reserva or inicio > fim_reserva) and destino == self.destino):
                quartosOcupados += 1
                self.numeroQuarto +=1    
                print("papapapappapapappapapapa")       # como o quarto 1 esta ocupado no proximo se encontrar ele ira "considerar" como quato 2
                if quartosOcupados == self.qtdQuartos:
                    return False
        return True
