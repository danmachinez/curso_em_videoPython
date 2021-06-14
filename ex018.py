from math import radians, cos, tan, sin
ang = float(input("Digite o valor do ângulo: "))
sen = sin(radians(ang))
cos = cos(radians(ang))
tang = tan(radians(ang))
print("O ângulo de {} tem o SENO de {:.2f}".format(ang, sen))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(ang, cos))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(ang, tang))
