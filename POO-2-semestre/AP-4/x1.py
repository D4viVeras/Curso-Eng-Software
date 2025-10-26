class Transporte:
    def __init__(self, marca, modelo, capacidade):
        self.marca = marca
        self.modelo = modelo
        self.capacidade = capacidade
    
    def get_marca(self):
        return self.marca
    def get_modelo(self):
        return self.modelo
    def get_capacidade(self):
        return self.capacidade
    def set_nova_marca(self, nova_marca):
        self.marca = nova_marca
    def set_novo_modelo(self, novo_modelo):
        self.modelo = novo_modelo
    def set_nova_capacidade(self, nova_capacidade):
        if nova_capacidade > 0:
            self.capacidade = nova_capacidade
        else:
            print("Capacidade deve ser maior que 0")
    def mostra_dados(self):
        print(f"Informações do Transporte\nMarca: {self.marca}\nModelo: {self.modelo}\nCapacidade: {self.capacidade} passageiros")
    
class TransporteTerrestre(Transporte):
    def __init__(self, marca, modelo, capacidade, numero_rodas=4):
        super().__init__(marca, modelo, capacidade)
        self.numero_rodas = numero_rodas
    
    def get_numero_rodas(self):
        return self.numero_rodas
    def set_novo_numero_rodas(self, novo_numero_rodas):
        if novo_numero_rodas >= 2:
            self.numero_rodas = novo_numero_rodas
        else:
            print("Veículos terrestres devem ter pelo menos 2 rodas")
    def mostra_dados(self):
        print(f"\nInformações do Transporte\nMarca: {self.marca}\nModelo: {self.modelo}\nCapacidade: {self.capacidade} passageiros\nNúmero de rodas: {self.numero_rodas}")

class TransporteAereo(Transporte):
    def __init__(self, marca, modelo, capacidade, numero_turbinas=2):
        super().__init__(marca, modelo, capacidade)
        self.numero_turbinas = numero_turbinas
    
    def get_numero_turbinas(self):
        return self.numero_turbinas
    def set_novo_numero_turbinas(self, novo_numero_turbinas):
        if novo_numero_turbinas >=1:
            self.numero_turbinas = novo_numero_turbinas
        else:
            print("Um transporte aéreo deve ter pleo menos uma turbina")
    def mostra_dados(self):
        print(f"\nInformações do Transporte\nMarca: {self.marca}\nModelo: {self.modelo}\nCapacidade: {self.capacidade} passageiros\nNúmero de turbinas: {self.numero_turbinas}")