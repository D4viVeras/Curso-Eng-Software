v1 = float(input("Digite o primeiro número:"))
v2 = float(input("Digite o segundo número:"))
v3 = float(input("Digite o terceiro número:"))

if v1>v2>v3:
    print("O maior número é:", v1)
elif v1>v3>v2:
    print("O maior número é:", v1)
elif v2>v1>v3:
    print("O maior número é:", v2)
elif v2>v3>v1:
    print("O maior número é:", v2)
elif v3>v1>v2:
    print("O maior número é:", v3)
elif v3>v2>v1:
    print("O maior número é:", v3)
elif v1>v2==v3:
    print("O maior número é:", v1)
elif v2>v1==v3:
    print("O maior número é:", v2)
elif v3>v2==v1:
    print("O maior número é:", v3)
elif v1<v2==v3:
    print("O maior número é:", v2)
elif v2<v1==v3:
    print("O maior número é:", v1)
elif v3<v1==v2:
    print("O maior número é:", v1)
else:
    print("O maior número é:", v1)