lista_animal = ['cachorro', 'gato', 'lobo', 'iguana', 'galinha']
print(lista_animal)
if 'papagaio' in lista_animal:
    print('Tem papagaio na lista')
else:
    a = input('Não tem um papagaio na lista. Adicionar papagaio? ')
    if a == 'Sim':
        lista_animal.append('papagaio')
    print(lista_animal)

b = input('Deseja remover papagaio? ')
if b == 'Sim':
    lista_animal.remove('papagaio')
    print(lista_animal)

c = input('Remover o último item da lista? ')
if c == 'Sim':
    lista_animal.pop()
    print(lista_animal)

d = input('Remover alguma posição específica da lista? ')
if d == str('Sim') or str('sim') or str('yes') or str('Yes'):
    e = input('Qual posição remover? ')
    if e == 'cachorro':
        lista_animal.pop(0)
        print(lista_animal)
    elif e == 'gato':
        lista_animal.pop(1)
    elif e == 'lobo':
        lista_animal.pop(2)
    elif e == 'iguana':
        lista_animal.pop(3)
    elif e == 'galinha':
        lista_animal.pop(4)
else:
    print(lista_animal)
# Lista em ordem alfabética:
print(lista_animal)
lista_animal.sort()
print(lista_animal)
# Reverter lista
lista_animal.reverse()
print(lista_animal)

# Uma lista imutável(tupla)
tupla = (1, 2, 5, 7, 8)

# Com a lsta noral podemos fazer alterações, com a tupla não.
# Len: dizer quantos itens tem em uma lista/tupla/conjunto

lista_animal[2] = 'gaivota'
print(lista_animal)
print(len(lista_animal))
print(len(tupla))

# Transformar lista em tupla
tupla_animal = tuple(lista_animal)
print(type(lista_animal))
print(lista_animal)

