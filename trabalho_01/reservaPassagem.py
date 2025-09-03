from datetime import datetime
class Passagem:

    agenda = []
    qtdPassagem = 2       #Numeros de passagems para o dia e local desejado

    def __init__(self,nome,origem ,destino, diaIda, diaVolta):
        self.nome = nome
        self.origem = origem
        self.destino = destino
        self.diaIda = datetime.strptime(diaIda, "%d/%m/%Y")
        self.diaVolta = datetime.strptime(diaVolta, "%d/%m/%Y")

        if self.verifica():

            self.agenda.append((self.nome, self.diaIda, self.diaVolta,self.origem, self.destino))
            print(f"passagem reservada no nome de: {self.nome}, para o dia: {diaIda} e retorno {diaVolta} de {self.origem} para {self.destino}")

        else:
            raise ValueError("Passagem não disponivel nesse periodo")

    def verifica(self):

        inicio = self.diaIda
        fim = self.diaVolta
        destino = self.destino
        origem = self.origem
        passagemEncontrada = 0

        for passagem in self.agenda:
            _, ini_passagem, fim_passagem, local_origem, local_destino = passagem
            # Se ja houver o registro de uma pasagem com o mesmo dia(ida ou volta) com os mesmos destinos entra no if
            if ((inicio == ini_passagem or fim == fim_passagem ) and (origem == local_origem and destino == local_destino )):
                passagemEncontrada +=1
                if passagemEncontrada == self.qtdPassagem:
                    return False
        return True