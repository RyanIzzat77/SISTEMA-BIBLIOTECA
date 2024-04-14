#método que lê os valores e adiciona na lista
def adicionaLivro():
    nome = str(input('Nome do livro: '))
    autor = str(input('Autor do livro: '))
    lista.append([nome, autor, False])

#método com loop que exibe todos os livros
def exibeLivros(lista):
    for item in lista:
        print(f'Titulo: {item[0]} ||| Autor: {item[1]} ||| Foi emprestado?: {item[2]}')

def emprestaLivro(lista):
    livro = input('Qual título deseja pegar emprestado: ').lower()
    temLivro = False #controle de código
    
    while not temLivro:
        for item in lista: #percorre toda a lista
            if livro == item[0].lower(): #verifica se o titulo é igual
                if item[2] == False: #verifica se o livro não foi emprestado, se for False é pq não foi emprestado ainda
                    temLivro = True #caso as condições acima forem verdadeiras, altera o valor de tem livro para True e encerra o loop
                    item[2] = True #coloca o status do livro como emprestado, True é pq o livro foi emprestado
                    print(f'Você alugou "{livro}"')
                    break
        if not temLivro: #caso não tenha o livro disponivel 
            print(f'{livro} não está disponivel para aluguel')
            break

def devolveLivro(lista):
    devolucao = str(input('Está devolvendo qual titulo: ').lower())
    temLivro = False #controle de codigo
    for item in lista: #percorre toda a lista
        if devolucao == item[0].lower(): #verifica se o titulo está na lista
            if item[2] == True: #verifica se o livro foi emprestado, True é pq foi emprestado
                item[2] = False #caso as duas condições forem verdadeiras, o livro será devolvido e o status de 'foi emprestado?' vira False
                temLivro = True #muda a variavel de controle para True e encerra o codigo
                print(f'{devolucao} foi devolvido, muito obrigado(a)')
                break   
            else: #caso tenha o titulo, mas o item[2] seja False, significa que tem o livro mas não foi emprestado
                print(f'O livro "{devolucao}" não está emprestado.')
                temLivro = True
                return
    if not temLivro: #caso o devolucao for diferente de item[0].lower (nome do livro) é pq o livro não existe na lista
        print(f'O livro "{devolucao}" não está disponível na biblioteca.')    

#criação da lista              
lista = []

#adicionando alguns itens
lista.append(['DonQuixote', 'Algum cara famoso', False])
lista.append(['Biblia Sagrada', 'vários autores', False])
lista.append(['Harry Potter', 'J.K Rowling', False])

try:
    #loop que chama os métodos
    while True:
        print('=-'*30)
        print('BIBLIOTECA DA UNICSUL')
        print('=-'*30)
        print('[1] Ver livros \n[2] Adicionar livro \n[3] Pegar livro emprestado \n[4] Devolver livro \n[5] Sair')
        print('-'*60)
        op = int(input('Selecione uma opção: '))

        if op == 1:
            exibeLivros(lista)
        elif op == 2:
            adicionaLivro()
        elif op == 3:
            emprestaLivro(lista)
        elif op == 4:
            devolveLivro(lista)
        elif op == 5:
            print('Encerrando...')
            break 
        else:
            print('opção inválida')        
except ValueError:
    print('opção inválida')     




