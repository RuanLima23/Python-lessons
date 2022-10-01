from aula9 import escrever_arquivo, atualizar_arquivo, ler_arquivo
import shutil

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        # Split serve para dividir o conteúdo da variável de acordo com as condições especificadas em cada parâmetro da função.
        aluno = lista_notas[0]
        print(aluno)
        lista_notas.pop(0)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 3
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/User/PycharmProjects')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/User/PycharmProjects')

if __name__ == '__main__':
    # move_arquivo('Notas 1º tri')
    # copia_arquivo('Notas 1º tri')
    # aluno = '\nJoao, 35, 20, 20, 90, 90'
    # atualizar_arquivo('Notas 1º tri', aluno)
    # lista_media = media_notas('Notas 1º tri')
    # print(lista_media)
