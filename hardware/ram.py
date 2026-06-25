from hardware.componentes import Componentes


class RAM(Componentes):
    """
    Memória principal de trabalho.
    Recebe a instrução do Disco para que a CPU possa acessá-la rapidamente.
    """

    def __init__(self):
        super().__init__("RAM")
        self.dados = None

    def carregar(self, dados):
        self.dados = dados
        print(f"{self} Instrução carregada: {dados}")

    def ler(self):
        return self.dados