class Componentes:

    """
    Classe base para todos os componentes do computador.
    Todo componente (CPU, RAM, Cache, Disco...) herda dela.
    """

    def __init__(self,nome):
        self.nome = nome

    def __str__(self):
        return f"[{self.nome}]"
