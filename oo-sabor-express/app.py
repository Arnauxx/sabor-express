from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
# restaurante_mexicano = Restaurante('mexican food', 'Mexicana')
# restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_praca.receber_avaliacao('Stevan', 10)
restaurante_praca.receber_avaliacao('Alice', 8)
restaurante_praca.receber_avaliacao('Naiala', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()