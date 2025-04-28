ct = 0
soma = 0
ctimp = 0
somaimp = 0
print("Digite [0] para sair")

while True:
    numeros = float(input("Digite um número:"))
    if numeros == 0:
        break
    if numeros%2 == 0:
        ct = ct +1
        soma = numeros + soma
    if numeros %2 != 0:
        ctimp = ctimp + 1
        somaimp = numeros + somaimp
if ct !=0:
    media = soma / ct
    print(f"A média dos  números pares é:{media:.2f}")
if ctimp !=0:
    mediaimp = somaimp / ctimp
    print(f"A média dos  números ímpares é:{mediaimp:.2f}")