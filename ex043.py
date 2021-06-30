altura = float(input('Digite sua altura em Metros: '))
peso = float(input('Digite seu peso em KG: '))

imc = peso / (altura ** 2) 

print(f'Seu IMC é de {imc:.1f}')

if imc < 18.5:
    print('Você está abaixo do seu peso ideal!')
elif 18.5 <= imc < 25:
    print('Você se encontra no seu peso ideal!')
elif 25 <= imc < 30:
    print('Você está com Sobrepeso!')
elif 30 <= imc < 40:
    print('Você está em Obesidade!')
else:
    print('Você está em Obesidade Mórbida, cuidado!')