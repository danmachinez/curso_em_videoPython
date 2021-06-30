valorDaCasa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salário do comprador? R$ '))
anosPagamento = int(input('Em quantos anos vai financiar? '))

maxPossivel = salario * 0.3
prestacoes = valorDaCasa / (anosPagamento * 12)

if prestacoes <= maxPossivel:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')