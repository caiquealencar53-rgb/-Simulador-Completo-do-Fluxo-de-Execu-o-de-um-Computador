import customtkinter as ctk
from tkinter import PhotoImage
from tkinter import Canvas
# Aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela
janela = ctk.CTk()
janela.title("Simulador Von Neumann")
janela.geometry("1000x700")

# ICONE COM TK
icone = PhotoImage(file="Login.png")
janela.iconphoto(True, icone)


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

    janela.after(1000, lambda: enviar_cache(dado))

def enviar_cache(dado):
    frame_ram.configure(fg_color=("gray20", "gray20"))

    frame_cache.configure(fg_color="green")
    label_cache.configure(text=f"CACHE\n{dado}")

def animar_fluxo():
    y = 200

    def mover():
        nonlocal y

        if y < 400:
            y += 2
            bola.place(x=500, y=y)
            frame_inicio.after(10, mover)
    
    mover()

def enviar():
    executar()
    animar_fluxo()
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
    width=200,
    height=50,
    text="Executar",
    command=iniciar
)
botao_inicio.pack(pady=100)


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
    command=enviar
)
botao_enviar.pack(pady=10)

# ==========================
# ÁREA DO FLUXO
# ==========================

fluxo = ctk.CTkFrame(frame_simulador)
fluxo.pack(pady=30)

# SSD
frame_ssd = ctk.CTkFrame(fluxo, width=250, height=80)
frame_ssd.grid(row=0, column=0)

label_ssd = ctk.CTkLabel(
    frame_ssd,
    text="SSD"
)
label_ssd.pack(expand=True)

# SETA 1
seta1 = ctk.CTkLabel(
    fluxo,
    text="↓",
    font=("Arial", 40)
)
seta1.grid(row=1, column=0)

# RAM
frame_ram = ctk.CTkFrame(fluxo, width=250, height=80)
frame_ram.grid(row=2, column=0)

label_ram = ctk.CTkLabel(
    frame_ram,
    text="RAM"
)
label_ram.pack(expand=True)

# SETA 2
seta2 = ctk.CTkLabel(
    fluxo,
    text="↓",
    font=("Arial", 40)
)
seta2.grid(row=3, column=0)

# CACHE
frame_cache = ctk.CTkFrame(fluxo, width=250, height=80)
frame_cache.grid(row=4, column=0)

label_cache = ctk.CTkLabel(
    frame_cache,
    text="CACHE"
)
label_cache.pack(expand=True)

frame_ssd.grid_propagate(False)
frame_ram.grid_propagate(False)
frame_cache.grid_propagate(False)

# Executa
janela.mainloop()