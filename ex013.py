print("-" * 29)
print(" CÁLCULO DE AUMENTO SALARIAL")
print("-" * 29)
salario = float(input("Digite o valor do sálario: R$ "))
aumento = salario + ( salario * 0.15 )
print("O valor do salário com o aumento de 15% é de {:.2f}.".format(aumento))
print()
resposta = input("Caso deseja calcular outros aumentos diga 'sim': ").upper().strip()[0]
if resposta == 'S':
    novo_salario = float(input("Digite o valor do salário: R$ "))
    valor_aumento = int(input("Digite o valor (em %) do aumento salarial: "))
    aumento_correto = valor_aumento / 100
    ns_aumentado = novo_salario * aumento_correto
    ns_final = novo_salario + ns_aumentado
    print("O valor do salário com o aumento de {}% é de {:.2f}.".format(valor_aumento, ns_final))
    print()
else:
    print("-" * 60)
    print("  OBRIGADO POR USAR NOSSA CALCULADORA DE AUMENTO SALARIAL")
    print("-" * 60)