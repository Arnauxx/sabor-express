import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza suprema', 'categoria':'Pizzaria', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_do_programa():
      print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def limpar_tela(texto = ''):
      '''Essa função é responsável por limpar o console para nova exibição'''
      os.system('cls')
      linha = '*' * (len(texto))
      print(linha)
      print(texto)
      print(linha)
      print()
      
def exibe_retorno_menu_principal():
      input('\nDigite uma tecla para voltar ao menu principal ')
      main()                        

def exibir_opcoes():
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Ativar restaurante')
      print('4. Sair\n')

def finalizar_app():
      limpar_tela('Encerrando aplicativo...')

def opcao_invalida(erro = ''):
      print(f'Opção inválida!\n erro: {erro}')      
      exibe_retorno_menu_principal()

def cadastrar_novo_restaurante():
      '''Essa função é responsável por cadastrar um novo restaurante
      
      Inputs: 
      - Nome do restaurante
      - Categoria do restaurante

      Outputs:
      - Adiciona um novo restaurante a lista de restaurante
      
      '''

      limpar_tela('Cadastro de novos restaurantes')
      nome_do_restaurante = input('Digite o nome do restaurante: ')
      categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
      dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo': False}
      restaurantes.append(dados_do_restaurante)
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
      exibe_retorno_menu_principal()

def listar_restaurantes():
      limpar_tela('Lista de restaurantes')

      print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

      exibe_retorno_menu_principal()

def alternar_status_restaurante():
      limpar_tela('Alterando status do restaurante')
      nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
      restaurante_encontrado = False

      for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                  restaurante_encontrado = True
                  restaurante['ativo'] = not restaurante['ativo']
                  mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
                  print(mensagem)

      if not restaurante_encontrado:
            print('O restaurante não foi encontrado')                             

                           
      exibe_retorno_menu_principal()                

def escolher_opcao():
      try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            if opcao_escolhida == 1:
                  cadastrar_novo_restaurante()
            elif opcao_escolhida == 2:
                  listar_restaurantes()
            elif opcao_escolhida == 3:
                  alternar_status_restaurante()
            elif opcao_escolhida == 4:
                  finalizar_app()           
            else:
                  opcao_invalida()
      except Exception as e:
            opcao_invalida(str(e))                     

def main():
      limpar_tela()
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcao()         

if __name__ == '__main__':
      main()
