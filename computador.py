from hardware.entrada import Entrada
from hardware.disco import Disco
from hardware.ram import RAM
from hardware.cache import Cache
from hardware.cpu import CPU
from hardware.saida import Saida


class Computador:
    """
    Orquestra todos os componentes de hardware na ordem correta.
    É o 'maestro': cada peça só sabe fazer a sua parte, e o
    Computador decide a ordem em que elas são chamadas.
    """

    def __init__(self):
        self.entrada = Entrada()
        self.disco = Disco()
        self.ram = RAM()
        self.cache = Cache()
        self.cpu = CPU()
        self.saida = Saida()

    def executar(self):
        # 1. Usuário digita a operação
        instrucao = self.entrada.receber()

        # 2. Salva no disco (armazenamento permanente)
        self.disco.salvar(instrucao)

        # 3. Carrega da disco para a RAM (memória de trabalho)
        self.ram.carregar(self.disco.ler())

        # 4. Verifica se já existe na cache (mais rápido que a CPU)
        resultado = self.cache.buscar(instrucao)

        if resultado is None:
            # 5. Cache miss -> CPU calcula de verdade
            resultado = self.cpu.calcular(self.ram.ler())
            # 6. Guarda na cache pra próxima vez ser mais rápido
            self.cache.salvar(instrucao, resultado)

        # 7. Mostra o resultado pro usuário
        self.saida.exibir(resultado)

    def processar(self, instrucao):
        """
        Versão do fluxo pensada para ser chamada pela interface gráfica.
        Não usa input()/print(): recebe a instrução como parâmetro e
        devolve o resultado junto com o histórico de cada etapa,
        para a interface poder exibir o passo a passo na tela.
        """
        passos = []

        passos.append(f"[Entrada] Recebido: {instrucao}")

        self.disco.salvar(instrucao)
        passos.append(f"[Disco] Instrução salva: {instrucao}")

        self.ram.carregar(self.disco.ler())
        passos.append(f"[RAM] Instrução carregada: {instrucao}")

        resultado = self.cache.buscar(instrucao)

        if resultado is None:
            passos.append("[Cache] Miss! Indo buscar na RAM...")
            resultado = self.cpu.calcular(self.ram.ler())
            passos.append(f"[CPU] Processando: {instrucao}")
            self.cache.salvar(instrucao, resultado)
        else:
            passos.append(f"[Cache] Hit! Resultado encontrado: {resultado}")

        passos.append(f"[Saída] Resultado: {resultado}")

        return resultado, passos