from x1 import Transporte, TransporteAereo, TransporteTerrestre

if __name__ == '__main__':
    transporte1 = Transporte("Volvo", "X-200", 50)
    transporte2 = TransporteTerrestre("Toyota", "Hilux", 5, 4)
    transporte3 = TransporteAereo("Boeing", "737 Max", 200, 2)

    transporte1.mostra_dados()
    transporte2.set_nova_capacidade(70)
    transporte3.mostra_dados()

    print(f"Marca transporte1: {transporte1.get_marca()}")
    print(f"Marca transporte2: {transporte2.get_modelo()}")

    terrestre1 = TransporteTerrestre("Toyota", "Hilux", 5, 4)
    terrestre2 = TransporteTerrestre("Fiat", "Uno", 4)

    terrestre1.mostra_dados()
    terrestre2.set_novo_numero_rodas(3)
    terrestre2.mostra_dados()

    aereo1 = TransporteAereo("Boeing", "737", 200, 2)
    aereo2 = TransporteAereo("Airbus", "A320", 180)

    aereo1.mostra_dados()
    aereo2.set_novo_numero_turbinas(1)
    aereo2.mostra_dados()

    print(f"Turbinas do aereo1: {aereo1.get_numero_turbinas()}")