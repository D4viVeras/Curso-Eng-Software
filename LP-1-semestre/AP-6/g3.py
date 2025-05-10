def soma3_num(v1, v2, v3):
    soma = v1 + v2 + v3
    return soma

if __name__ == '__main__':
    v1 = float(input("Digite um número:"))
    v2 = float(input("Digite outro número:"))
    v3 = float(input("Agora digite o último número:"))
    soma_retorno = soma3_num(v1, v2, v3)
    print("A soma dos três números digitados é:", soma_retorno)