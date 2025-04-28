l1 = float(input("Digite o valor do primeiro lado:"))
l2 = float(input("Digite o valor do segundo lado:"))
l3 = float(input("Digite o valor do terceiro lado:"))
if l1==l2+l3 or l2==l1+l3 or l3==l1+l2:
    print("Não é um triângulo!")
else:
    if l1 < l2 + l3:
        if l1 == l2 == l3:
            print("É um triângulo equilátero!")
        elif l1 == l2 != l3 or l1 != l2 == l3 or l1 == l3 != l2:
            print("É um triângulo isósceles!")
        else:
            print("É um triângulo escaleno!")