import os

livros = [{'titulo':'Dom Casmurro', 'autor':'Machado de Assis', 'disponivel':False}, 
          {'titulo':'1984', 'autor':'George Orwell', 'disponivel':True},
          {'titulo':'O Pequeno Príncipe', 'autor':'Antoine de Saint-Exupéry', 'disponivel':False}]

def exibir_nome_do_programa():
    print("""
╔══════════════════════════╗
║  SISTEMA DE GERENCIAMENTO ║
║        DE LIVROS          ║
╚══════════════════════════╝
""")


def exibir_opcoes():
    print('1. Cadastrar livro')
    print('2. Listar livros')
    print('3. Alternar disponibilidade do livro')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('App Finalizado =)')

def voltar_ao_menu_principal():
    input('\nDigite enter para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_livro():
    exibir_subtitulo('Cadastro de novos livros')
    titulo_do_livro = input('Digite o título do livro que deseja cadastrar: ')
    autor = input(f'Digite o nome do autor do livro {titulo_do_livro}: ')
    dados_do_livro = {'titulo':titulo_do_livro, 'autor':autor, 'disponivel':False}
    livros.append(dados_do_livro)
    print(f'O livro {titulo_do_livro} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_livros():
    exibir_subtitulo('Listando livros')

    print(f"{'Título do livro'.ljust(22)} | {'Autor'.ljust(20)} | Status")
    for livro in livros:
        titulo_livro = livro['titulo']
        autor = livro['autor']
        disponivel = 'disponível' if livro['disponivel'] else 'indisponível'
        print(f"- {titulo_livro.ljust(20)} | {autor.ljust(20)} | {disponivel}")

    voltar_ao_menu_principal()

def alternar_disponibilidade_livro():
    exibir_subtitulo('Alterando disponibilidade do livro')
    titulo_livro = input('Digite o título do livro que deseja alterar a disponibilidade: ')
    livro_encontrado = False

    for livro in livros:
        if titulo_livro == livro['titulo']:
            livro_encontrado = True
            livro['disponivel'] = not livro['disponivel']
            mensagem = f'O livro {titulo_livro} agora está disponível' if livro['disponivel'] else f'O livro {titulo_livro} agora está indisponível'
            print(mensagem)
            
    if not livro_encontrado:
        print('O livro não foi encontrado')
            
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_novo_livro()
        elif opcao_escolhida == 2: 
            listar_livros()
        elif opcao_escolhida == 3: 
            alternar_disponibilidade_livro()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
