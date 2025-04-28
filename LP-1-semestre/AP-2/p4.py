v1 = float(input("Digite um valor:"))
v2 = float(input("Digite outro valor:"))
simbolo = input("Operações aceitas: + - * /\nDigite o símbolo da operação:")
if simbolo == "+":
    print("A soma dos valores escolhidos é:", v1+v2)
elif simbolo == "-":
    print("A subtração dos valores escolhidos é:", v1-v2)
elif simbolo == "*":
    print("A multiplicação dos valores escolhidos é:", v1*v2)
else:
    print("A divisão dos valores escolhidos é:", v1/v2)