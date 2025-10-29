class Animal:
    def __init__(self, nome, idade, habitat):
        self.nome = nome
        self.idade = idade
        self.habitat = habitat
    
    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
    def get_habitat(self):
        return self.habitat
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self.idade = nova_idade
        else:
            print("Erro: O animal deve ter no mínimo 1 ano")
    def set_habitat(self, novo_habitat):
        self.habitat = novo_habitat
    def emitir_som(self):
        print(f"{self.nome} emite um som genérico")

class Mamifero(Animal):
    def __init__(self, nome, idade, habitat, pelagem, amamenta="sim"):
        super().__init__(nome, idade, habitat)
        self.pelagem = pelagem
        self.amamenta = amamenta

    def get_pelagem(self):
        return self.pelagem
    def get_amamenta(self):
        return self.amamenta
    def set_pelagem(self, nova_pelagem):
        self.pelagem = nova_pelagem
    def set_amamenta(self, novo_amamenta):
        self.amamenta = novo_amamenta

class Aves(Animal):
    def __init__(self, nome, idade, habitat, penas, pode_voar="sim"):
        super().__init__(nome, idade, habitat)
        self.penas = penas
        self.pode_voar = pode_voar

    def get_penas(self):
        return self.penas
    def get_pode_voar(self):
        return self.pode_voar
    def set_penas(self, novo_penas):
        self.penas = penas 
    def set_pode_voar(self, novo_pode_voar):
        self.pode_voar = pode_voar

