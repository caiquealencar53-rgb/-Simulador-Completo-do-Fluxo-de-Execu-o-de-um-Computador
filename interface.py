import tkinter as tk
from tkinter import font

from computador import Computador


class InterfaceGrafica:
    """
    Camada de interface (Tkinter).
    Importante: essa classe NÃO sabe como CPU, RAM, Cache etc.
    funcionam por dentro. Ela só chama pc.processar() e mostra
    o que volta na tela. Toda a lógica fica isolada no Computador.
    """

    def __init__(self, root):
        self.pc = Computador()

        self.root = root
        self.root.title("Simulador do Fluxo de Execução de um Computador")
        self.root.geometry("520x480")
        self.root.configure(bg="#1e1e2e")

        self.icone = tk.PhotoImage(file="Login.png")
        self.root.iconphoto(False, self.icone)

        fonte_titulo = font.Font(family="Segoe UI", size=14, weight="bold")
        fonte_normal = font.Font(family="Consolas", size=11)

        # ---------- Título ----------
        titulo = tk.Label(
            root, text="Calculadora — Fluxo de Execução",
            font=fonte_titulo, bg="#1e1e2e", fg="#cdd6f4"
        )
        titulo.pack(pady=(15, 5))

        # ---------- Campo de entrada ----------
        frame_entrada = tk.Frame(root, bg="#1e1e2e")
        frame_entrada.pack(pady=10)

        self.entry_operacao = tk.Entry(
            frame_entrada, font=fonte_normal, width=25,
            bg="#313244", fg="#cdd6f4", insertbackground="#cdd6f4",
            relief="flat"
        )
        self.entry_operacao.pack(side="left", padx=(0, 10), ipady=5)
        self.entry_operacao.insert(0, "5 + 3")
        self.entry_operacao.bind("<Return>", lambda evento: self.executar())

        botao_executar = tk.Button(
            frame_entrada, text="Executar", font=fonte_normal,
            bg="#89b4fa", fg="#1e1e2e", relief="flat",
            activebackground="#74a8f5", cursor="hand2",
            command=self.executar
        )
        botao_executar.pack(side="left")

        # ---------- Resultado em destaque ----------
        self.label_resultado = tk.Label(
            root, text="Resultado: —",
            font=font.Font(family="Segoe UI", size=18, weight="bold"),
            bg="#1e1e2e", fg="#a6e3a1"
        )
        self.label_resultado.pack(pady=15)

        # ---------- Log do fluxo (passo a passo) ----------
        label_log = tk.Label(
            root, text="Fluxo de execução:",
            font=fonte_normal, bg="#1e1e2e", fg="#9399b2"
        )
        label_log.pack(anchor="w", padx=20)

        self.text_log = tk.Text(
            root, height=12, font=fonte_normal,
            bg="#181825", fg="#cdd6f4", relief="flat",
            state="disabled", wrap="word"
        )
        self.text_log.pack(padx=20, pady=(5, 20), fill="both", expand=True)

    def executar(self):
        instrucao = self.entry_operacao.get().strip()

        if not instrucao:
            return

        # ÚNICA chamada de lógica: tudo que acontece de "hardware"
        # fica escondido dentro do Computador.
        resultado, passos = self.pc.processar(instrucao)

        self.label_resultado.config(text=f"Resultado: {resultado}")
        self._atualizar_log(passos)

    def _atualizar_log(self, passos):
        self.text_log.config(state="normal")
        self.text_log.delete("1.0", tk.END)

        for linha in passos:
            self.text_log.insert(tk.END, linha + "\n")

        self.text_log.config(state="disabled")

def main():
    root = tk.Tk()
    InterfaceGrafica(root)
    root.mainloop()


if __name__ == "__main__":
    main()