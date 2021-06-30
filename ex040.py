primeiraNota = float(input('Qual a primeira nota? '))
segundaNota = float(input('Qual a segunda nota? '))
mediaAluno = (primeiraNota + segundaNota) / 2
print(mediaAluno)
if mediaAluno < 5:
    print('Aluno REPROVADO!')
elif 5 < mediaAluno < 6.9:
    print('Aluno em RECUPERAÇÃO!')
else:
    print('Aluno APROVADO!')