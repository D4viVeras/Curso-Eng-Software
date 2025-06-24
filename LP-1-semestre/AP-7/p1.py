def valor(v1):
    if v1>0:
        print("Valor positivo!")
    elif v1==0:
        print("Valor nulo!")
    else:
        print("Valor negativo!")

if __name__ == '__main__':
    v1 = float(input(("Digite um número:")))
    valor(v1)