class Supermercado(object):
    def __init__(self, produto, validade, quantidade, preco):
        self.produto = produto
        self.validade = validade
        self.quantidade = quantidade
        self.preco = preco
    
    def get_produto(self):
        return self.produto
    def get_validade(self):
        return self.validade
    def get_quantidade(self):
        return self.quantidade
    def get_preco(self):
        return self.preco
    def set_produto(self, novo_produto):
        self.produto = novo_produto
    def set_validade(self, nova_validade):
        self.validade = nova_validade
    def set_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade
    def set_preco(self, novo_preco):
        self.preco = novo_preco
    def mostra_dados(self):
        print(f"Produto: {self.produto} \n Validade: {self.validade} \n Quantidade: {self.quantidade} \n Preço: {self.preco}")
    def retorna_dados(self):
        retornar  = f"Produto: {self.produto} \n Validade: {self.validade} \n Quantidade: {self.quantidade} \n Preço: {self.preco}"
        return retornar
    def aumenta_preco(self, aumento):
        self.preco += aumento

if __name__ == '__main__':
    produto1 = Supermercado("Banana", 2025, 12, 14.90)
    produto2 = Supermercado("Maçã", 2025, 1, 1.20)
    produto3 = Supermercado("Melancia", 2025, 1, 12.70)
produto1.mostra_dados()
print(f"Produto: {produto2.get_produto()} \nValidade: {produto2.get_validade()} \nQuantidade: {produto2.get_quantidade()} \nPreço: {produto2.get_preco()}")
print(produto3.retorna_dados())
aumento = float(input("Digite o aumento do preço do produto: "))
produto2.aumenta_preco(aumento)
print(f"O valor atual do produto {produto2.get_produto()} é: {produto2.get_preco()}")
produto1.set_produto('Uva')
produto1.set_validade(2025)
produto1.set_quantidade(1)
produto1.set_preco(7.9)
produto1.mostra_dados()