contador = 0
soma = 0
media = 0
numero_20 = 0

print('Digite [0] para sair')
while True:
    numero = float(input("Digite um número:"))
    if numero == 0:
        break
    if numero != 0:
        contador = contador +1
        soma = numero + soma
        media = soma / contador
    if numero > 20:
        numero_20 = numero_20 + 1

print("Quantidade de números digitados:", contador)
print("Soma dos números digitados:", soma)
print("A médias dos números digitados:", media)
print("A quantidade de números maiores que 20 são:", numero_20)