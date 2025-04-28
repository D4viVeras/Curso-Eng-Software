soma = 0
for x in range(0,501,3):
    if x % 2 != 0:
        print(x)
        soma = soma + x
print("A soma dos números é:",soma)