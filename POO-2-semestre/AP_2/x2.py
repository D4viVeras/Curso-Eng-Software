class Casa(object):
    def __init__(self, cidade, comodo, andar, preco):
        self.cidade = cidade
        self.comodo = comodo
        self.andar = andar
        self.preco = preco
    
    def get_cidade(self):
        return self.cidade
    def get_comodo(self):
        return self.comodo
    def get_andar(self):
        return self.andar
    def get_preco(self):
        return self.preco
    def set_cidade(self, nova_cidade):
        self.cidade = nova_cidade
    def set_comodo(self, novo_comodo):
        self.comodo = novo_comodo
    def set_andar(self, novo_andar):
        self.andar = novo_andar
    def set_preco(self, novo_preco):
        self.preco = novo_preco
    def mostra_dados(self):
        print(f"Cidade: {self.cidade} \n Quantidade de cômodos da casa: {self.comodo} \nQuantidade de andares da casa: {self.andar} \n Preço: {self.preco}")
    def retorna_dados(self):
        retornar  = f"Cidade: {self.cidade} \n Quantidade de cômodos da casa: {self.comodo} \n Quantidade de andares da casa: {self.andar} \n Preço: {self.preco}"
        return retornar
    def aumenta_preco(self, aumento):
        self.preco += aumento

if __name__ == '__main__':
    casa1 = Casa("Borges", 7, 2, 299000.90)
    casa2 = Casa("Bela Vista", 6, 1, 235000.20)
    casa3 = Casa("Hotbronks", 9, 2, 1200000.70)
casa1.mostra_dados()
print(f"Cidade: {casa2.get_cidade()} \nQuantidade de cômodos da casa: {casa2.get_comodo()} \nQuantidade de andares da casa: {casa2.get_andar()} \nPreço: {casa2.get_preco()}")
print(casa3.retorna_dados())
aumento = float(input("Digite o aumento do preço da casa: "))
casa2.aumenta_preco(aumento)
print(f"A cidade atual da casa {casa2.get_cidade()} é: {casa2.get_preco()}")
casa1.set_cidade('Rocha Pompers')
casa1.set_andar(2)
casa1.set_comodo(8)
casa1.set_preco(700000.9)
casa1.mostra_dados()