lista = []

print("Digite [-1] para sair!")
while True:
    n1 = float(input("Digite a nota do aluno: "))
    if n1 == -1:
        break
    if n1 != -1:
        lista.append(n1)
print(f"A média da turma foi: {sum(lista)/len(lista)}, sendo que têm {len(lista)} alunos na turma!")
