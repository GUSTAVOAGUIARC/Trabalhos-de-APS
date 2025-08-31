from facadeReserva import FacadeReserva

def main():
                        #para facilitar estou considerando que so tenha 1 carro, aviao para 1 pessoa e o hotel so tenha 1 quarto para ser facil de forçar um erro
   cliente = {
    'nome': 'Gustavo',
    'origem': 'Rio',
    'destino': 'SP',
    'diaIda': '16/09/2001',
    'diaVolta': '17/09/2001',
}
   
   cliente2 = {
    'nome': 'Felipe Coltinho',
    'origem': 'Rio',
    'destino': 'SP',
    'diaIda': '16/09/2001',
    'diaVolta': '17/09/2001',
}
   cliente3 = {
    'nome': 'Vegetti',
    'origem': 'RO',
    'destino': 'BA',
    'diaIda': '16/09/2001',
    'diaVolta': '19/10/2001',
}

   FacadeReserva(cliente).reservarTudo()
   FacadeReserva(cliente2).reservarCarro()
   FacadeReserva(cliente2).reservarPassagem()
   FacadeReserva(cliente3).reservarHotel()
   FacadeReserva(cliente3).reservarPassagem()


if __name__ == "__main__":
    main()