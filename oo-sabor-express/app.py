from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('mexican food', 'Mexicana')
# restaurante_japones = Restaurante('Japa', 'Japonesa')

print(restaurante_praca.receber_avaliacao('Stevan', 10))
print(restaurante_praca.receber_avaliacao('Alice', 0))
print(restaurante_praca.receber_avaliacao('Naiala', 5))
print(restaurante_praca.receber_avaliacao('Noah', 1))


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()