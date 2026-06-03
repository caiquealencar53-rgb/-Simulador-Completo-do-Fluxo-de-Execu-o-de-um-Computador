import customtkinter as ctk


# aparencia

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# janela

janela = ctk.CTk()
janela.title("Simulador Von Neumann")
janela.geometry("1000x700")

# titulo

titulo = ctk.CTkLabel(
    janela,
    text="Arquitetura de Von Neumann",
    font=("Arial", 24, "bold")
)

titulo.pack(pady=20)

# botão

botao = ctk.CTkButton(
    janela,
    text="Executar"
)

botao.pack(pady=10)

janela.mainloop()