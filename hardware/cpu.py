from hardware.componentes import Componentes


class CPU(Componentes):
    """
    Processador: quem realmente executa o cálculo.
    Só é chamada quando a Cache não tem o resultado (cache miss).
    """

    def __init__(self):
        super().__init__("CPU")

    def calcular(self, instrucao):
        try:
            resultado = eval(instrucao)  # ex: eval("5 + 3") -> 8
            return resultado
        except Exception:
            return "Erro: operação inválida"