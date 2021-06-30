from datetime import date
anoAtual = date.today().year

anoNascimento = int(input('Digite o ano de nascimento do atleta: '))
idadeAtleta = anoAtual - anoNascimento
print()
print(f'A idade do atleta é de {idadeAtleta} anos!')

if idadeAtleta <= 9:
    print('CATEGORIA: MIRIM')
elif idadeAtleta <= 14:
    print('CATEGORIA: INFANTIL')
elif idadeAtleta <= 19:
    print('CATEGORIA: JÚNIOR')
elif idadeAtleta <= 25:
    print('CATEGORIA: SÊNIOR')
else:
    print('CATEGORIA: MASTER')
