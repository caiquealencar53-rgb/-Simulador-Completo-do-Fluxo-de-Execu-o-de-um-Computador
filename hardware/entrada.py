from hardware.componentes import Componentes

   
"""
    Representa o teclado / usuário digitando a operação.
    Responsabilidade única: capturar o que o usuário digitou.
    """


class Entrada(Componentes):
    def __init__(self):
        super().__init__("Entrada")
    
    def receber(self):
        dados = input("Digite os dados de entrada (ex 5 + 3): ")
        print(f"{self} Recebido {dados}")
        return dados