from time import sleep
print("-" * 50)
print("  DESCUBRA QUANTO PAGARÁ APÓS O DESCONTO DE 5%")
print("-" * 50)
valor_original = float(input("Digite o valor do produto: R$ "))
valor_descontado = valor_original * 0.05
valor_final = valor_original - valor_descontado
print("O valor de seu produto com os 5% descontados é de: R$ {:.2f}".format(valor_final))
print("-" * 63)
sleep(2)
resposta = (int(input("Caso queira calcular mais descontos, digite 'sim':"))
if resposta == 'sim':
    novo_valor = float(input("Digite o valor do novo produto: R$ "))
    valor_do_desconto = int(input("Digite o valor (em %) para calcular o seu desconto: "))
    desconto_correto = valor_do_desconto / 100
    nv_descontado = novo_valor * desconto_correto
    print("O valor descontado foi: R$ {:.2f}".format(nv_descontado))
    nv_final = novo_valor - nv_descontado
    print("O valor do seu produto após o desconto de {}% é de R$ {:.2f}.".format(valor_do_desconto, nv_final))
    print()
else:
print("-" * 50)
print("  OBRIGADO POR USAR NOSSA CALCULADORA DE DESCONTOS")
print("-" * 50)