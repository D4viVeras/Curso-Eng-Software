num = int(input("Digite um número inteiro:"))
num2 = int(input("Ele será multiplicado até que número:"))
for x in range(1,num2+1,1):
    y = x * num
    print(x,"x", num, "=",y)