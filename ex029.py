velocidade = float(input('Qual é a velocidade atual do seu carro? '))
multa = 7 * (velocidade - 80)
if velocidade > 80:
    print('\033[1;31mMULTADO! Você excedeu o limite de permitido que é de 80Km/h\nVocê deve pagar uma multa de R${:.2f}!\033[m'.format(multa))
print('\033[1;36mTenha um bom dia! Dirija com segurança!\033[m')
