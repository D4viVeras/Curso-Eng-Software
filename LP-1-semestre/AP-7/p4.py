def fatorial(n):
    n0 = 1
    for n in range(1, n+1, 1):
        n0 = n0*n
    return n0

if __name__ == '__main__':
    n = int(input("Digite o número que você gostaria de saber o fatorial:"))
    retorno = fatorial(n)
    print("O valor do fatorial que você digitou é:", retorno)