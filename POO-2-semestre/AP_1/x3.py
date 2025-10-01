class Concessionária(object):
    def __init__(self, carro, ano, valor):
        self.carro = carro
        self.ano = ano
        self.valor = valor
    
    def get_carro(self):
        return self.carro
    def get_ano(self):
        return self.ano
    def get_valor(self):
        return self.valor
    def set_carro(self, novo_carro):
        self.carro = novo_carro
    def set_ano(self, novo_ano):
        self.ano = novo_ano
    def set_valor(self, novo_valor):
        self.valor = novo_valor
    def mostra_dados(self):
        print(f"Carro: {self.carro} \n Ano: {self.ano} \n Valor: {self.valor}")

if __name__ == '__main__':
    carro1 = Concessionária('Aventador SVJ', '2020/2021', 'R$ 9,400,000' )
    carro2 = Concessionária('Ferrari PuroSangue', '2024/2025', 'R$ 8,900,000' )
    carro3 = Concessionária('Ferrari 21Cilindri', '2024/2025', 'R$ 8,700,000' )
    carro4 = Concessionária('Rolls-Royce Cullinan', '2024/2024', 'R$ 8,200,000' )
    
    carro1.mostra_dados()
    carro2.mostra_dados()
    carro3.mostra_dados()
    carro4.mostra_dados()
    print(f"Carro: {carro1.get_carro()} \n Ano: {carro1.get_ano()} \n Valor: {carro1.get_valor()}")
    print(f"Carro: {carro2.get_carro()} \n Ano: {carro2.get_ano()} \n Valor: {carro2.get_valor()}")
    print(f"Carro: {carro3.get_carro()} \n Ano: {carro3.get_ano()} \n Valor: {carro3.get_valor()}")
    print(f"Carro: {carro4.get_carro()} \n Ano: {carro4.get_ano()} \n Valor: {carro4.get_valor()}")