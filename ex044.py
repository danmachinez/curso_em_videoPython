valorProduto = float(input('Digite o valor a ser pago: R$ '))

print('''Confira as condições de pagamentos a seguir:
    [1] À vista (Dinheiro ou Cheque): 10% de desconto
    [2] À vista no Cartão: 5% de desconto
    [3] Em até 2x no cartão: preço cheio
    [4] 3x ou mais no cartão: 20% de juros''')

meioDePagamento = input('Como gostaria de efetuar o pagamento? [1-4]\n')
while meioDePagamento not in '1234':
    meioDePagamento = input('CONDIÇAÕ DE PAGAMENTO NÃO IDENTIFICADA! Como gostaria de efetuar o pagamento? [1-4]\n')
if meioDePagamento == '1':
    valorFinal = valorProduto - (valorProduto * 0.10)
    print(f'O valor do produto é de R${valorProduto:.2f} e com o desconto ficará: R${valorFinal:.2f}')
elif meioDePagamento == '2':
    valorFinal = valorProduto - (valorProduto * 0.05)
    print(f'O valor do produto é de R${valorProduto:.2f} e com o desconto ficará: R${valorFinal:.2f}')
elif meioDePagamento == '3':
    valorFinal = valorProduto
    print(f'O valor do produto é de R${valorFinal:.2f}')
else:
    valorFinal = valorProduto + (valorProduto * 0.20)
    print(f'O valor do produto é de R${valorProduto:.2f} e com os juros ficará: R${valorFinal:.2f}')
    

