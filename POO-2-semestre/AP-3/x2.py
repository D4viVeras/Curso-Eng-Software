from x1 import Aluno, Professor

if __name__ == '__main__':
    aluno1 = Aluno("Adalberto", 5)
    aluno2 = Aluno("Benício", 4)
    professor1 = Professor("Clarencio", 7, 3)
    professor2 = Professor("Dennis", 8, 2)

    print(f"Nome do aluno: {aluno1.get_nome()}\nQuantidade de aulas deste aluno por semana: {aluno1.get_qtd_aulas()}")
    print(f"\nNome do aluno: {aluno2.get_nome()}\nQuantidade de aulas deste aluno por semana: {aluno2.get_qtd_aulas()}")
    print(f"\nNome do professor: {professor1.get_nome()}\nQuantidade de aulas deste professor por semana: {professor1.get_qtd_aulas()}\nQuantidade de turmas deste professor: {professor1.get_qtd_turmas()}")
    print(f"\nNome do professor: {professor2.get_nome()}\nQuantidade de aulas deste professor por semana: {professor2.get_qtd_aulas()}\nQuantidade de turmas deste professor: {professor2.get_qtd_turmas()}")
    aluno1.mostra_dados()
    professor1.mostra_dados()
    aluno2.saudacao()
    professor2.saudacao()