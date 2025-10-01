
def soma():
    print(f"A soma dos números digitados é: {num1+num2}")
def subtracao():
    print(f"A subtração dos números digitados é: {num1-num2}")
def multiplicacao():
    print(f"A multiplicação dos números digitados é: {num1 * num2}")
def divisao():
    print(f"A divisão dos números digitados é: {num1/num2}")    
if __name__ == '__main__':
    operacao = input("+ - x / \nDigite a operação de sua escolha:").lower()
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    if operacao == '+':
        soma()
    elif operacao == '-':
        subtracao()
    elif operacao == 'x':
        multiplicacao()
    elif operacao == '/':
        divisao()
    else:
        print("Escolha uma operação válida!")