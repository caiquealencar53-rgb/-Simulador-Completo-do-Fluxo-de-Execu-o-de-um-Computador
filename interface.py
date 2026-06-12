import customtkinter as ctk
from cpu import CPU
from memoria import Memoria
from tkinter import PhotoImage


class Interface:
    def __init__(self):
        # Tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Janela
        self.janela = ctk.CTk()
        self.janela.geometry("900x680")
        self.janela.title("⚙  Simulador Von Neumann")
        self.janela.resizable(False, False)

        try:
            icone = PhotoImage(file="Login.png")
            self.janela.iconphoto(True, icone)
        except:
            pass

        # Estado
        self.operacao_selecionada = None
        self.resultado_final = None
       
        self.cpu = CPU()
        self.ssd = Memoria("SSD")
        self.ram = Memoria("RAM")
        self.cache = Memoria("CACHE")

        # Monta as telas
        self.criar_tela_inicio()
        self.criar_tela_simulador()

    # ──────────────────────────────────────────────
    # TELA INICIAL
    # ──────────────────────────────────────────────
    def criar_tela_inicio(self):
        self.frame_inicio = ctk.CTkFrame(self.janela, fg_color="#1a1a2e")
        self.frame_inicio.pack(fill="both", expand=True)

        ctk.CTkLabel(
            self.frame_inicio,
            text="⚙  Simulador Von Neumann",
            font=("Courier New", 28, "bold"),
            text_color="#00d4ff"
        ).pack(pady=60)

        ctk.CTkLabel(
            self.frame_inicio,
            text="Visualize o fluxo de dados pela hierarquia de memória\naté o processamento na CPU.",
            font=("Arial", 14),
            text_color="#aaaaaa",
            justify="center"
        ).pack(pady=10)

        ctk.CTkButton(
            self.frame_inicio,
            width=220, height=55,
            text="Iniciar Simulação",
            font=("Arial", 16, "bold"),
            fg_color="#00d4ff",
            hover_color="#0099bb",
            text_color="#000000",
            corner_radius=12,
            command=self.iniciar
        ).pack(pady=60)

    def iniciar(self):
        self.frame_inicio.pack_forget()
        self.frame_simulador.pack(fill="both", expand=True)

    # ──────────────────────────────────────────────
    # TELA DO SIMULADOR
    # ──────────────────────────────────────────────
    def criar_tela_simulador(self):
        self.frame_simulador = ctk.CTkFrame(self.janela, fg_color="#1a1a2e")

        ctk.CTkLabel(
            self.frame_simulador,
            text="⚙  Fluxo de Dados",
            font=("Courier New", 22, "bold"),
            text_color="#00d4ff"
        ).pack(pady=(18, 4))

        self.criar_calculadora()
        self.criar_fluxo()

    # ──────────────────────────────────────────────
    # CALCULADORA
    # ──────────────────────────────────────────────
    def criar_calculadora(self):
        frame_calc = ctk.CTkFrame(
            self.frame_simulador,
            fg_color="#12122a", corner_radius=14,
            border_width=2, border_color="#333366"
        )
        frame_calc.pack(pady=(4, 10), padx=30, fill="x")

        ctk.CTkLabel(
            frame_calc, text="CALCULADORA",
            font=("Courier New", 11, "bold"), text_color="#555599"
        ).pack(pady=(10, 2))

        # Entradas
        frame_entradas = ctk.CTkFrame(frame_calc, fg_color="transparent")
        frame_entradas.pack(pady=4)

        self.entry_1 = ctk.CTkEntry(
            frame_entradas, width=130, height=34,
            placeholder_text="Número 1",
            border_color="#334466", font=("Courier New", 13)
        )
        self.entry_1.grid(row=0, column=0, padx=8)

        self.label_op_display = ctk.CTkLabel(
            frame_entradas, text="?",
            font=("Courier New", 22, "bold"),
            text_color="#00d4ff", width=30
        )
        self.label_op_display.grid(row=0, column=1, padx=4)

        self.entry_2 = ctk.CTkEntry(
            frame_entradas, width=130, height=34,
            placeholder_text="Número 2",
            border_color="#334466", font=("Courier New", 13)
        )
        self.entry_2.grid(row=0, column=2, padx=8)

        # Botões de operação
        frame_ops = ctk.CTkFrame(frame_calc, fg_color="transparent")
        frame_ops.pack(pady=(4, 8))

        self.botoes_op = []
        ops = [("+", "+"), ("-", "−"), ("*", "×"), ("/", "÷")]
        for i, (op, simbolo) in enumerate(ops):
            b = ctk.CTkButton(
                frame_ops, width=70, height=34,
                text=simbolo, font=("Courier New", 18, "bold"),
                fg_color="#1a1a2e", hover_color="#1e3a5f",
                border_color="#334466", border_width=1, corner_radius=8,
                command=lambda o=op, s=simbolo: self.selecionar_op(o, s)
            )
            b.grid(row=0, column=i, padx=6)
            self.botoes_op.append((b, simbolo))

        # Botão enviar
        self.botao_enviar = ctk.CTkButton(
            frame_calc, width=180, height=36,
            text="▶  Enviar para CPU",
            font=("Arial", 13, "bold"),
            fg_color="#00d4ff", hover_color="#0099bb",
            text_color="#000000", corner_radius=10,
            command=self.executar
        )
        self.botao_enviar.pack(pady=(0, 12))

        self.entry_1.bind("<Return>", lambda e: self.executar())
        self.entry_2.bind("<Return>", lambda e: self.executar())

    def selecionar_op(self, op, simbolo):
        self.operacao_selecionada = op
        self.label_op_display.configure(text=simbolo)
        for b, s in self.botoes_op:
            b.configure(
                fg_color="#1e3a5f" if s == simbolo else "#1a1a2e",
                border_width=2 if s == simbolo else 1
            )

    # ──────────────────────────────────────────────
    # FLUXO DE COMPONENTES
    # ──────────────────────────────────────────────
    def criar_fluxo(self):
        frame_fluxo = ctk.CTkFrame(self.frame_simulador, fg_color="transparent")
        frame_fluxo.pack(pady=4, expand=True)

        frame_col = ctk.CTkFrame(frame_fluxo, fg_color="transparent")
        frame_col.pack(side="left", padx=30)

        self.componentes = {}
        itens = [
            ("ssd",   "💾  SSD",   0),
            ("ram",   "🧮  RAM",   1),
            ("cache", "⚡  CACHE", 2),
            ("cpu",   "🔲  CPU",   3),
        ]
        for chave, nome, linha in itens:
            f = ctk.CTkFrame(frame_col, width=200, height=68,
                             fg_color="#16213e", corner_radius=10,
                             border_color="#334466", border_width=2)
            f.grid(row=linha * 2, column=0, pady=2)
            f.grid_propagate(False)

            lbl_nome = ctk.CTkLabel(f, text=nome,
                                    font=("Courier New", 13, "bold"),
                                    text_color="#00d4ff")
            lbl_nome.pack(pady=(8, 0))

            lbl_dado = ctk.CTkLabel(f, text="aguardando...",
                                    font=("Courier New", 10),
                                    text_color="#778899")
            lbl_dado.pack()

            if linha < 3:
                ctk.CTkLabel(frame_col, text="↓", font=("Arial", 22),
                             text_color="#334466").grid(row=linha * 2 + 1, column=0)

            self.componentes[chave] = (f, lbl_nome, lbl_dado)

        # Painel de output
        frame_out = ctk.CTkFrame(frame_fluxo, width=220, height=320,
                                 fg_color="#12122a", corner_radius=14,
                                 border_color="#334466", border_width=2)
        frame_out.pack(side="left", padx=30, anchor="center")
        frame_out.pack_propagate(False)

        ctk.CTkLabel(frame_out, text="OUTPUT",
                     font=("Courier New", 11, "bold"),
                     text_color="#555599").pack(pady=(20, 4))

        self.lbl_expr    = ctk.CTkLabel(frame_out, text="—",
                                        font=("Courier New", 15),
                                        text_color="#aaaacc")
        self.lbl_expr.pack(pady=4)

        self.lbl_resultado = ctk.CTkLabel(frame_out, text="---",
                                          font=("Courier New", 32, "bold"),
                                          text_color="#00d4ff")
        self.lbl_resultado.pack(pady=12)

        self.lbl_status = ctk.CTkLabel(frame_out, text="",
                                       font=("Arial", 11),
                                       text_color="#778899")
        self.lbl_status.pack(pady=4)

        frame_log = ctk.CTkFrame(frame_out, fg_color="#0d0d1f",
                                 corner_radius=8, width=190, height=120)
        frame_log.pack(pady=10, padx=14, fill="x")
        frame_log.pack_propagate(False)

        self.lbl_log = ctk.CTkLabel(frame_log, text="",
                                    font=("Courier New", 9),
                                    text_color="#446688",
                                    justify="left", anchor="nw")
        self.lbl_log.pack(padx=6, pady=6, fill="both", expand=True)

        self.log_linhas = []

    # ──────────────────────────────────────────────
    # LÓGICA DE EXECUÇÃO
    # ──────────────────────────────────────────────
    def log(self, msg):
        self.log_linhas.append(msg)
        if len(self.log_linhas) > 7:
            self.log_linhas.pop(0)
        self.lbl_log.configure(text="\n".join(self.log_linhas))

    def resetar(self):
        nomes = {"ssd": "💾  SSD", "ram": "🧮  RAM",
                 "cache": "⚡  CACHE", "cpu": "🔲  CPU"}
        for chave, (f, lbl_n, lbl_d) in self.componentes.items():
            f.configure(fg_color="#16213e", border_color="#334466")
            lbl_n.configure(text=nomes[chave], text_color="#00d4ff")
            lbl_d.configure(text="aguardando...", text_color="#778899")

    def ativar(self, chave, dado, cor="#00d4ff"):
        f, lbl_n, lbl_d = self.componentes[chave]
        f.configure(fg_color=cor, border_color=cor)
        lbl_d.configure(text=dado, text_color="#000000" if cor == "#00d4ff" else "#ffffff")

    def concluir(self, chave, dado):
        f, lbl_n, lbl_d = self.componentes[chave]
        f.configure(fg_color="#16213e", border_color="#00aa55")
        lbl_d.configure(text=f"✓ {dado}", text_color="#00aa55")

    def executar(self):
        if self.operacao_selecionada is None:
            self.lbl_status.configure(text="⚠ Selecione uma operação!", text_color="#ff6666")
            return
        try:
            n1 = float(self.entry_1.get())
            n2 = float(self.entry_2.get())
        except ValueError:
            self.lbl_status.configure(text="⚠ Entradas inválidas!", text_color="#ff6666")
            return
        if self.operacao_selecionada == "/" and n2 == 0:
            self.lbl_status.configure(text="⚠ Divisão por zero!", text_color="#ff6666")
            return

        simbolos = {"+": "+", "-": "−", "*": "×", "/": "÷"}
        sim = simbolos[self.operacao_selecionada]
        expr = f"{n1:g} {sim} {n2:g}"
       
        self.ssd.armazenar(expr)
        self.ram.armazenar(expr)
        self.cache.armazenar(expr)

        self.resultado_final = self.cpu.executar(
            n1,
            n2,
            self.operacao_selecionada
        )

        self.botao_enviar.configure(state="disabled")
        self.lbl_resultado.configure(text="...", text_color="#445566")
        self.lbl_expr.configure(text=expr)
        self.lbl_status.configure(text="processando...", text_color="#778899")
        self.log_linhas.clear()
        self.lbl_log.configure(text="")
        self.resetar()

        def etapa(chave, msg, cor, duracao, proximo):
            self.log(msg)
            self.ativar(chave, expr, cor)
            self.janela.after(duracao, lambda: [self.concluir(chave, expr), self.janela.after(300, proximo)])

        def cpu_final():
            res = self.resultado_final
            res_str = f"{res:g}" if abs(res) < 1e9 and res == int(res) else f"{res:.4f}"
            self.log(f"[OUT]  resultado = {res_str}")
            f, lbl_n, lbl_d = self.componentes["cpu"]
            f.configure(fg_color="#00aa55", border_color="#00aa55")
            lbl_d.configure(text=f"= {res_str}", text_color="#ffffff")
            self.lbl_resultado.configure(text=res_str, text_color="#00d4ff")
            self.lbl_expr.configure(text=f"{expr} =")
            self.lbl_status.configure(text="✓ Concluído", text_color="#00aa55")
            self.botao_enviar.configure(state="normal")

        # Encadeia as 4 etapas
        e4 = lambda: (self.log("[CPU]  executando ULA..."),
                      self.ativar("cpu", "PROCESSANDO...", "#ff9900"),
                      self.janela.after(1200, cpu_final))
        e3 = lambda: etapa("cache", "[CACHE] instrução em espera", "#00d4ff", 900, e4)
        e2 = lambda: etapa("ram",   "[RAM]  carregando operandos", "#00d4ff", 900, e3)
        e1 = lambda: etapa("ssd",   f"[SSD]  lendo: {expr}",       "#00d4ff", 900, e2)
        e1()

    # ──────────────────────────────────────────────
    # INICIAR
    # ──────────────────────────────────────────────
    def inicializar(self):
        self.janela.mainloop()


# Ponto de entrada
if __name__ == "__main__":
    app = Interface()
    app.inicializar()