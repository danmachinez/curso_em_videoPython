distancia = float(input('Qual a distância de sua viagem? '))
print('Você está se preparando para uma viagem de \033[4m{}Km\033[m '.format(distancia))
if distancia <= 200:
  preço = distancia * 0.50
else:
  preço = distancia * 0.45
print('E o preço de sua passagem será de \033[4;32mR${:.2f}\033[m'.format(preço))