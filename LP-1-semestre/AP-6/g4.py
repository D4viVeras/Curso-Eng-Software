print("Este problema resolverá esta função: x+3y")

def calculadora(x, y):
    resultado = x + 3*y
    return resultado

if __name__ == '__main__':
    x = float(input("Digite o valor de x:"))
    y = float(input("Agora o de y:"))
    resultado_retorno = calculadora(x, y)
    print(f"Este é o resultado com duas casas decimais: {resultado_retorno:.2f}")