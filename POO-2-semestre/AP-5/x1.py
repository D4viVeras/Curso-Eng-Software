class Publicacao:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self. autor = autor
    
    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    def set_titulo(self, novo_titulo):
        if len(novo_titulo)>3:
            self.titulo = novo_titulo
        else:
            print("O título deve ter pelo menos três caracteres!")
    def set_autor(self, novo_autor):
        self.autor = novo_autor

class Livro(Publicacao):
    def __init__(self, titulo, autor, genero):
        super().__init__(titulo, autor)
        self.genero = genero

    def get_genero(self):
        return self.genero
    def set_genero(self, novo_genero):
        self.genero = novo_genero

class Revista(Publicacao):
    def __init__(self, titulo, autor, edicao):
        super().__init__(titulo, autor)
        self.edicao = edicao

    def get_edicao(self):
        return self.edicao
    def set_edicao(self, nova_edicao):
        if nova_edicao < 1:
            print("O número da edição deve ser pelo menos: 1")
        else:
            self.edicao = nova_edicao