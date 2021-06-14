print("-" * 55)
print("SAIBA QUANTO DE TINTA PRECISARIA PARA PINTAR SUA PAREDE")
print("-" * 55)
lar = float(input("Digite a largura de sua parede: "))
alt = float(input("Digite a altura de sua parede: "))
area = lar * alt
litros = area / 2
print("A dimensão de sua parede é de {} x {} e sua área é de {}m²".format(lar, alt, area))
print("Você vai precisar de {}L de tinta para pintar uma parede.".format(litros))
print("-" * 55)
#por função if e continuar
#print("Caso queira calcular outros valores diga 'sim'")