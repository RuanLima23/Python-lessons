# Representamos a lista com colchetes( [ ] ), tupla com Parenteses ( ) e o conjunto com chaves ({ }).

conjunto = {1, 2, 3, 4, 5, 9}
conjunto2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Une os conjuntos
a = conjunto.union(conjunto2)
print('União: {}'.format(a))

# Elementos repetidos nos conjuntos
b = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(b))

# Elementes diferentes nos conjuntos
c = conjunto2.difference(conjunto)
print('Diferença: {}'.format(c))

# Elementos diferentes em ambos os conjuntos
d = conjunto2.symmetric_difference(conjunto)
print('Diferença simétrica: {}'.format(d))

# Subconjunto, conjunto menor onde todos os seus elemnetos se encontram no conjunto maior
e = conjunto.issubset(conjunto2)
print('O conjunto 1 é um subconjunto do conjunto 2? {}'.format(e))

f = conjunto2.issubset(conjunto2)
print('O conjunto 2 é um subconjunto do conjunto 1? {}'.format(f))

# Superconjunto, conjunto maior que comporta todos os elementos do conjunto maior tendo ainda mais elementos
g = conjunto.issuperset(conjunto2)
print('O conjunto 1 é um superconjunto do conjunto 2? {}'.format(g))

h = conjunto2.issuperset(conjunto)
print('O conjunto 2 é um superconjunto do conjunto 1? {}'.format(h))

# Converter lista e tupla para conjunto
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'galinha']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)

