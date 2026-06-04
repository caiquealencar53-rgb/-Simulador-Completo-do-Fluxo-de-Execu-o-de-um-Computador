import customtkinter as ctk

# Aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela
janela = ctk.CTk()
janela.title("Simulador Von Neumann")
janela.geometry("1000x700")


# ==========================
# FUNÇÕES
# ==========================

def iniciar():
    frame_inicio.pack_forget()
    frame_simulador.pack(fill="both", expand=True)


def executar(event=None):
    dado = entrada.get()

    if dado == "":
        return

    # SSD recebe o dado
    label_ssd.configure(text=f"SSD\n{dado}")
    frame_ssd.configure(fg_color="green")

    # Após 1 segundo vai para RAM
    janela.after(1000, lambda: enviar_ram(dado))


def enviar_ram(dado):
    frame_ssd.configure(fg_color=("gray20", "gray20"))

    frame_ram.configure(fg_color="green")
    label_ram.configure(text=f"RAM\n{dado}")


# ==========================
# TELA INICIAL
# ==========================

frame_inicio = ctk.CTkFrame(janela)
frame_inicio.pack(fill="both", expand=True)

titulo = ctk.CTkLabel(
    frame_inicio,
    text="Arquitetura de Von Neumann",
    font=("Arial", 24, "bold")
)
titulo.pack(pady=40)

botao_inicio = ctk.CTkButton(
    frame_inicio,
    text="Executar",
    command=iniciar
)
botao_inicio.pack(pady=20)


# ==========================
# TELA DO SIMULADOR
# ==========================

frame_simulador = ctk.CTkFrame(janela)

titulo_simulador = ctk.CTkLabel(
    frame_simulador,
    text="Fluxo de Dados",
    font=("Arial", 20, "bold")
)
titulo_simulador.pack(pady=20)

entrada = ctk.CTkEntry(
    frame_simulador,
    width=300,
    placeholder_text="Digite uma instrução"
)
entrada.pack(pady=10)

# Enter executa
entrada.bind("<Return>", executar)

botao_enviar = ctk.CTkButton(
    frame_simulador,
    text="Enviar",
    command=executar
)
botao_enviar.pack(pady=10)

# SSD
frame_ssd = ctk.CTkFrame(
    frame_simulador,
    width=250,
    height=80
)
frame_ssd.pack(pady=20)

label_ssd = ctk.CTkLabel(
    frame_ssd,
    text="SSD"
)
label_ssd.pack(expand=True)

# RAM
frame_ram = ctk.CTkFrame(
    frame_simulador,
    width=250,
    height=80
)
frame_ram.pack(pady=20)

label_ram = ctk.CTkLabel(
    frame_ram,
    text="RAM"
)
label_ram.pack(expand=True)

# Mantém tamanho dos frames
frame_ssd.pack_propagate(False)
frame_ram.pack_propagate(False)

# Executa
janela.mainloop()