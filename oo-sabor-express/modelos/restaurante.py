from modelos.avaliacao import Avaliacao

class Restaurante:
    """Representa um restaurante e suas características."""
    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """        
        self._nome: str = nome.title()
        self._categoria: str = categoria.upper()
        self._ativo: bool = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Retorna uma representação em string do restaurante."""        
        return f'{self._nome.ljust(25)} | {self._categoria.ljust(25)} | {str(self.media_avaliacoes).ljust(25)} | {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""        
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(restaurante)

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""        
        return '✔️' if self._ativo else '❌'
    
    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """        
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
            return f'Avaliação incluída com sucesso!!!'
        else:
            return f'Valor da nota inválido somente é permitido o valor de 1 a 5'

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""        
        if not self._avaliacao:
            return f'-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media        

