n = int(input("Digite um número:"))
ct = 0
for x in range(n,-1,-1):
    ct += 1
    print(x)
print("A quantidade de números gerados foi:", ct)
