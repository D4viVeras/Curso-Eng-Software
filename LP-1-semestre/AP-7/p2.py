def valorabsoluto(v1):
    if v1>=0:
        print("O módulo deste número é:", v1)
    else:
        print("O módulo deste número é:", v1*-1)

if __name__ == '__main__':
    v1 = float(input(("Digite um número:")))
    valorabsoluto(v1)