import os

restaurantes = ['Pizza', 'Sushi']

def exibir_nome_do_programa():
      print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def limpar_tela():
      os.system('cls')

def exibe_retorno_menu_principal():
      input('\nDigite uma tecla para voltar ao menu principal')
      main()                        

def exibir_opcoes():
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Ativar restaurante')
      print('4. Sair\n')

def finalizar_app():
      limpar_tela()
      print('Encerrando aplicativo...\n')

def opcao_invalida():
      print('Opção inválida!\n')      
      exibe_retorno_menu_principal()

def cadastrar_novo_restaurante():
      limpar_tela()
      print('Cadastro de novos restaurantes\n')
      nome_do_restaurante = input('Digite o nome do restaurante: ')
      restaurantes.append(nome_do_restaurante)
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
      exibe_retorno_menu_principal()

def listar_restaurantes():
      limpar_tela()
      print('Lista de restaurantes\n')

      for restaurante in restaurantes:
            print(f'.{restaurante}')

      exibe_retorno_menu_principal()          

def escolher_opcao():
      try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            if opcao_escolhida == 1:
                  cadastrar_novo_restaurante()
            elif opcao_escolhida == 2:
                  listar_restaurantes()
            elif opcao_escolhida == 3:
                  print('Ativar restaurante')
            elif opcao_escolhida == 4:
                  finalizar_app()           
            else:
                  opcao_invalida()
      except:
            opcao_invalida()                     

def main():
      limpar_tela()
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcao()         

if __name__ == '__main__':
      main()
