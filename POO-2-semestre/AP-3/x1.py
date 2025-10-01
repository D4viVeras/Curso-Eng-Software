class Aluno:
    def __init__(self, nome, qtd_aulas):
        self.nome = nome
        self.qtd_aulas = qtd_aulas

    def get_nome(self):
        return self.nome
    def get_qtd_aulas(self):
        return self.qtd_aulas
    def set_novo_nome(self, novo_nome):
        self.nome = self.novo_nome
    def set_nova_qtd_aulas(self, nova_qtd_aulas):
        if nova_qtd_aulas <0:
            print("A quantidade de aulas não pode ser negativa!")
        else:
            self.qtd_aulas = self.nova_qtd_aulas
    def mostra_dados(self):
        print(f"Aluno\nNome do: {self.nome}\nQuantidade de aulas: {self.qtd_aulas}")
    def saudacao(self):
        print(f"Olá! Meu nome é: {self.nome} e tenho {self.qtd_aulas} aulas por semana!")

class Professor(Aluno):
    def __init__(self, nome, qtd_aulas, qtd_turmas):
        super().__init__(nome, qtd_aulas)
        self.qtd_turmas = qtd_turmas

    def get_qtd_turmas(self):
        return self.qtd_turmas
    def set_nova_qtd_turmas(self, nova_qtd_turmas):
        if nova_qtd_turmas <1:
            print("O professor deve ter pelo menos uma turma!")
        else:
            self.qtd_turmas = self.nova_qtd_turmas
    def mostra_dados(self):
        print(f"Professor\nNome: {self.nome}\nQuantidade de aulas: {self.qtd_aulas}\nQuantidade de turmas: {self.qtd_turmas}")