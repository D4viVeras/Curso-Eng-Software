fahrenheit1 = int(input("Digite o começo da variação da temperatura, medida em Fahrenheit:"))
fahrenheit2= int(input("Agora a medição final:"))
for fahrenheit in range(fahrenheit1, fahrenheit2+1, 1):
    celsius = (fahrenheit-32)/1.8
    print(f"{fahrenheit:.2f}ºF|{celsius:.2f}ºC)")