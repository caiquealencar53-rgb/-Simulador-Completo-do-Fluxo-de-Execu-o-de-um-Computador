from hardware.componentes import Componentes


class Disco(Componentes):

    def __init__(self):
        super().__init__("Disco")
        self.dados_armazenados = None

    def salvar(self, dados):
        self.dados_armazenados = dados
        print(f"{self} Instrução salva: {dados}")

    def ler(self):
        return self.dados_armazenados