cta = 0 #Contador de aprovados
ctr = 0 #Contador de reprovados
ct = 0 #Contador dos que fizeram a prova
print('Digite [-1] para sair')

while True:
    nota = float(input("Digite a sua nota:"))
    if nota == -1:
        break
    if nota >= 5:
        cta = cta +1
    if nota < 5:
        ctr = ctr + 1
    ct = ct +1
print('A quantidade de alunos aprovados:', cta)
print('A quantidade de alunos reprovados:', ctr)
print('A quantidade de alunos que fizeram a prova:', ct)