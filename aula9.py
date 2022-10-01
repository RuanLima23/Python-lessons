# # Criar um arquivo e escrever(w)

    # arquivo = open('teste.txt', 'w')
    # arquivo.write('Primeira linha')
    # arquivo.write('\nSegunda linha')
    # arquivo.close()

# # Atualizar um arquivo(a)

    # arquivo = open('teste.txt', 'a')
    # arquivo.write('\nTerceira linha')
    # arquivo.close()

def escrever_arquivo(texto):
    diretorio = 'C:/Users/User/PycharmProjects/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    atualizar_arquivo('C:/Users/User/PycharmProjects/teste.txt', '\n')
    escrever_arquivo('Primeira linha.\n')
    aluno = '\nFelipe, 7, 8, 5, 5'
    atualizar_arquivo('Notas.txt', aluno)
    ler_arquivo('teste.txt')