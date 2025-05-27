class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome: str = nome
        self.categoria: str = categoria
        self._ativo: bool = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome.ljust(25)} | {self.categoria.ljust(25)} | {self.ativo}'
    
    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(restaurante)

    @property
    def ativo(self):
        return '✔️' if self._ativo else '❌'


restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza', 'Pizzaria')

Restaurante.listar_restaurantes()





