sexo = input("Digite o seu sexo:")
altura = float(input("Digite a sua altura:"))
if sexo == "masculino" or sexo == "Masculino" or sexo == "MASCULINO":
    peso = (72.7* altura) -58
    print(f"O seu peso ideal é: {peso:.2f} Kg")
else:
    peso = (62.1 * altura) - 44.7
    print(f"O seu peso ideal é: {peso:.2f} Kg")