def soma(v1,v2):
    print(v1+v2)
def subtrai(v1,v2):
    print(v1-v2)
def multiplica(v1,v2):
    print(v1*v2)
def divisão(v1,v2):
    print(v1/v2)

if __name__ == '__main__':
    v1 = float(input(("Digite um número:")))
    v2 = float(input(("Digite um número:")))
    op = input("Operaçãoes disponíveis: + - x /\nDigite a operação desejada:")
    if op == "+":
        soma(v1, v2)
    elif op == "-":
        subtrai(v1, v2)
    elif op == "x":
        multiplica(v1, v2)
    else:
        divisão(v1,v2)