from hardware.componentes import Componentes


class Saida(Componentes):
    """
    Representa a tela/monitor.
    Responsabilidade única: mostrar o resultado final pro usuário.
    """

    def __init__(self):
        super().__init__("Saída")

    def exibir(self, resultado):
        print(f"{self} Resultado: {resultado}")