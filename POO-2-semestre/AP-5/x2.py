from x1 import Publicacao, Livro, Revista

if __name__ == '__main__':
    p1 = Publicacao("O Pequeno Príncipe", "Criança Galega")
    l1 = Livro("Livro de Ciências", "Alguém Inteligente", "Deixar de ser burro")
    r1 = Revista("Catálogo Boticário", "Boticário", 1)

    print(p1.get_autor(), p1.get_titulo())
    print(l1.get_autor(), l1.get_titulo(), l1.get_genero())
    print(r1.get_autor(), r1.get_titulo(), r1.get_edicao())

