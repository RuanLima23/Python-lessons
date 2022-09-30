
lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    divisao = 10 / 1
    numero = lista[1]

except ZeroDivisionError:
    print('Não pe possivel realizar uma divisão por zero')
except ArithmeticError:
    print('Houve um erro ao realizar uma opreção aritmética')
except IndexError:
    print('Erro ao acessar um índece inválido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Tudo normal, sem excessões')

finally:
    print('Sempre excuta, com ou sem erro')
    print('Fechando arquivo')
    arquivo.close()