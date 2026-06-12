class Registrador:
    def __init__(self, nome):
        self.nome = nome
        self.valor = None

    def carregar(self, valor):
        self.valor = valor

    def limpar(self):
        self.valor = None