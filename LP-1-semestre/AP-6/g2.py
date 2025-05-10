def calc_idade(idade_agr):
    idade = 2025 - ano_nasc
    return idade

if __name__ == '__main__':
    ano_nasc = int(input("Digite o seu ano de nascimento:"))
    ano_retorno = calc_idade(ano_nasc)
    print("Você tem", ano_retorno, "anos!")
