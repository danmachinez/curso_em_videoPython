num = int(input('Digite um número inteiro que deseja convertes: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

escolhaConversao = (input('Qual sua oção de conversão? '))
while escolhaConversao not in '123':
    escolhaConversao = (input('ESCOLHA INVÁLIDA! Qual sua oção de conversão? '))
if escolhaConversao == '1':
    print(f'O número {num} convertido para BÍNARIO é {bin(num)[2:]}')
elif escolhaConversao == '2':
    print(f'O número {num} convertido para OCTAL é {oct(num)[2:]}')    
elif escolhaConversao == '3':
    print(f'O número {num} convertido para HEXADECIMAL é {hex(num)[2:]}')