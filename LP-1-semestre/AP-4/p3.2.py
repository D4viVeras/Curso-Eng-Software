ct = 0
soma = 0

for x in range(2 ,21 , 2):
    ct = ct + 1
    print(x)
    soma = soma + x
media = soma / ct
print("A soma dos números é:", soma)
print("A média dos números é:", media)