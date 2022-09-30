from aula7_televisão import TV
from aula7_calculadora1 import Calculadora
from aula8_listaletras import contador_letras


if __name__ == '__main__':
    tv = TV()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)
    print(tv.canal)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    print(contador_letras(lista))