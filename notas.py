# print('Insira as notas individuais de cada aluno do primeiro trimestre.')
# a = int(input('Nota 1: '))
# if a > 25:
#     int(input('Valor não permitido. Nota 1: '))
# b = int(input('Nota 2: '))
# if b > 25:
#     int(input('Valor não permitido. Nota 2: '))
# c = int(input('Nota 3: '))
# if c > 50:
#     int(input('Valor não permitido. Nota 3: '))
# d = int(input('Nota 4: '))
# if d > 100:
#     int(input('Valor não permitido. Not 4: '))
# e = int(input('Nota 5: '))
# if e > 100:
#     int(input('Valor não permitido. Nota 5: '))
# media1 = (a + b + c + d + e) / 3
# print('Nota final: {}.'.format(media1))
# if media1 < 70:
#     print('O aluno está abaixo da média.')
# else:
#     print('O aluno está acima da média.')
# print('Insira as notas individuais de cada aluno do segundo trimestre.')
# A = int(input('Nota 1: '))
# if A > 25:
#     int(input('Valor não permitido. Nota 1: '))
# B = int(input('Nota 2: '))
# if B > 25:
#     int(input('Valor não permitido. Nota 2: '))
# C = int(input('Nota 3: '))
# if C > 50:
#     int(input('Valor não permitido. Nota 3: '))
# D = int(input('Nota 4: '))
# if D > 100:
#     int(input('Valor não permitido. Not 4: '))
# E = int(input('Nota 5: '))
# if E > 100:
#     int(input('Valor não permitido. Nota 5: '))
# media2 = (A + B + C + D + E) / 3
# print('Nota final: {}.'.format(media2))
# if media2 < 70:
#     print('O aluno está abaixo da média.')
# else:
#     print('O aluno está acima da média.')
# print('Insira as notas individuais de cada aluno do terceiro trimestre.')
# f = int(input('Nota 1: '))
# if f > 25:
#     int(input('Valor não permitido. Nota 1: '))
# g = int(input('Nota 2: '))
# if g > 25:
#     int(input('Valor não permitido. Nota 2: '))
# h = int(input('Nota 3: '))
# if h > 50:
#     int(input('Valor não permitido. Nota 3: '))
# i = int(input('Nota 4: '))
# if i > 100:
#     int(input('Valor não permitido. Not 4: '))
# j = int(input('Nota 5: '))
# if j > 100:
#     int(input('Valor não permitido. Nota 5: '))
# media3 = (f + g + h + i + j) / 3
# print('Nota final: {}.'.format(media3))
# if media3 < 70:
#     print('O aluno está abaixo da média.')
# else:
#     print('O aluno está acima da média.')
# mediafinal = (media1 + media2 + media3) / 3
# if mediafinal < 70:
#     print('O aluno reprovou, precisa passar pelo conselho.')
# else:
#     print('O aluno foi aprovado.')

a = int(input('Primeira nota: '))
b = int(input('Segunda nota '))
c = int(input('Terceira nota: '))
mediafinal = (a + b + c) / 3
if a <= 10 and b <= 10 and c <= 10:
    print('Média final: {}'.format(mediafinal))
    if mediafinal < 7:
        print('O aluno está reprovado!')
    else:
        print('O aluno está aprovado!')
else:
    print('Há notas informadas que não correspondem ao sistema, por favor tente novamente.')
