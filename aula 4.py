a = int(input('Entre com um número: '))
div = 0

for x in range(1, a+1):
    resto = a % x
    print(a, '/', x, '%', resto)
    if resto == 0:
        div = div + 1
        #ou (div += 1)
if div == 2:
    print('O número {} é primo.'.format(a))
else:
    print('O número {} não é primo.'.format(a))
# a = int(input('Entre com um valor: '))
#
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         # print(a, '/', x, '%', resto)
#         if resto == 0:
#             div = div + 1
#             #ou (div += 1)
#     if div == 2:
#         print(num)

# a = 0
# while a <= 10:
#     print(a)
#     a = a + 1
# b = int(input('Nota primeiro bimestre: '))
# while b > 10:
#     b = int(input('Nota acima de 10, insira novamente: '))
# else:
#     print('Insira a nota do segundo bimestre')
#
# nota = int(input('Insira a nota: '))
# while nota > 10:
#     nota = int(input('Insira a nota: '))








