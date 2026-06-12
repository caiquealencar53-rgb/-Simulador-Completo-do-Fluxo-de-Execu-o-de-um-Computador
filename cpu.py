# cpu.py

from ula import ULA

class CPU:

    def __init__(self):
        self.ula = ULA()

    def executar(self, n1, n2, op):

        resultado = self.ula.calcular(
            n1,
            n2,
            op
        )

        return resultado