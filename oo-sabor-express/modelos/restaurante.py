class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome: str = nome
        self.categoria: str = categoria
        self.ativo: bool = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(restaurante)



restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza', 'Pizzaria')

Restaurante.listar_restaurantes()





