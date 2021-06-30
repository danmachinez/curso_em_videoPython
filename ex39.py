from datetime import date
anoAtual = date.today().year

anoNascimento = int(input('Digite seu ano de nascimento: '))
idade = anoAtual - anoNascimento

if idade == 18:
    print('Você deverá se alistar esse ano!')
elif idade < 18:
    difAnos = 18 - idade
    print(f'Ainda faltam {difAnos} anos para você se alistar!')
elif idade > 18:
    difAnos = idade - 18
    print(f'Já passou da hora de você se alistar há {difAnos} anos')