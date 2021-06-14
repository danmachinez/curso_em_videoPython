salario = float(input('Qual o salário do funcionário? R$ '))
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print('Quem ganhava R$ {:.2f} passou a ganhar R$ {:.2f} agora'.format(salario, aumento))