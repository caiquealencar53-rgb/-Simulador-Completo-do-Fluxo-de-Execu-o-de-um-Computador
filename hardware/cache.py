from hardware.componentes import Componentes


class Cache(Componentes):
    """
    Memória rápida que guarda resultados já calculados.
    Se a mesma operação for repetida, devolve o resultado na hora
    (cache hit), sem precisar acionar a CPU de novo.
    """

    def __init__(self):
        super().__init__("Cache")
        self.historico = {}  # ex: {"5 + 3": 8}

    def buscar(self, instrucao):
        return self.historico.get(instrucao)

    def salvar(self, instrucao, resultado):
        self.historico[instrucao] = resultado