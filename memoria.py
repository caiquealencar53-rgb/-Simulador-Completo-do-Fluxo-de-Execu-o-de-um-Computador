class Memoria:

    def __init__(self, nome):
        self.nome = nome
        self.dados = []

    def armazenar(self, valor):
        self.dados.append(valor)

    def ler(self):
        return self.dados[-1]