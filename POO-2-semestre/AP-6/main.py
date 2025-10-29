from x1 import Animal, Mamifero, Aves

if __name__ == '__main__':
    an1 = Animal("Jacaré", 6, "Rio")
    m1 = Mamifero("Baleia", 12, "Mar", "Não")
    av1 = Aves("Arara", 4, "Floresta", "Azul")

    print(f"Status do primeiro animal:\nNome: {an1.get_nome()}\nIdade: {an1.get_idade()}\nHabitat: {an1.get_habitat()}")
    print(f"\nStatus do primeiro mamífero:\nNome: {m1.get_nome()}\nIdade: {m1.get_idade()}\nHabitat: {m1.get_habitat()}\nStatus da pelagem: {m1.get_pelagem()}\nAmamenta: {m1.get_amamenta()}")
    print(f"\nStatus da primeira ave:\nNome: {av1.get_nome()}\nIdade: {av1.get_idade()}\nHabitat: {av1.get_habitat()}\nStatus das penas: {av1.get_penas()}\nPode voar: {av1.get_pode_voar()}")

    m1.emitir_som()
    av1.emitir_som()
    an1.emitir_som()

