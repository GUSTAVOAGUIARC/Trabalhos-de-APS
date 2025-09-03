from facadeReserva import FacadeReserva

def main():
                                                        # a princio estou considerando que existe 1 carro por local
                                                        # 2 quartos por local
                                                        # 1 passageiro somente por local de partida --> destino
                                                        # porem e possivel mudar essa quantidade nas classes 
   cliente = {
    'nome': 'Gustavo',
    'origem': 'Brasil',            # utlizar somente a sicla do estado não esta sendo feita nenha veificação para ver se o usuario digitou coretamente
    'destino': 'USA',
    'diaIda': '16/09/2001',
    'diaVolta': '17/09/2001',
}
   
   cliente1 = {
    'nome': 'Felipe Coltinho',
    'origem': 'Brasil',
    'destino': 'argentina',
    'diaIda': '18/09/2001',
    'diaVolta': '19/09/2001',
}
   cliente2 = {
    'nome': 'Vegetti',
    'origem': 'Brasil',
    'destino': 'frança',
    'diaIda': '18/09/2001',
    'diaVolta': '19/10/2001',
}

   FacadeReserva(cliente).reservarTudo()
   FacadeReserva(cliente1).reservarTudo()
   FacadeReserva(cliente2).reservarTudo()

    # FacadeReserva(#####).reservarTudo()
    #FacadeReserva(#####).reservarCarro()
    # FacadeReserva(######).reservarHotel()
    # FacadeReserva(######).reservarPassagem()


if __name__ == "__main__":
    main()