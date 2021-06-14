numero = int(input('Digite um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é \033[1;34mPAR!\033[m'.format(numero))
else:
    print('O número {} é \033[1;33mÍMPAR!\033[m'.format(numero))