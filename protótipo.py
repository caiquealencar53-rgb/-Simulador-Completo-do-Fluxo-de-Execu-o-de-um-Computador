from customtkinter import *
from tkinter import PhotoImage

tela = CTk()
tela.geometry("750x500")

#Configurações da tela cor titulo e etc
tela.title("App_Teste")
tela.config(background="#282828")

#ícone
icone = PhotoImage(file="Login.png") 
tela.iconphoto(True, icone)

#Função butões
def Calcular(operação):
    try:
        n1 = float(entry.get())
        n2 = float(entry_2.get())
        
        if operação == "adição":
            resultado = n1 + n2
        elif operação == "subtração":
            resultado = n1 - n2
        elif operação == "multiplicação":
            resultado = n1 * n2
        elif operação == "divisão":
            resultado = n1 / n2
        label_2.configure(text = (resultado))
    except:
        label_2.configure(text = "Erro! entrada inválida")

#função tela filha

#Título
label = CTkLabel(
    tela,
    text="Fluxo de dados",
    text_color="#83a598",
    font= ("Arial", 30,"bold"),
    bg_color= "#282828"
)
label.pack(pady = 20)



#Caixa de texto
entry = CTkEntry(tela,width = 200, height=30, placeholder_text="Digite aqui",border_color="#98971a")
entry.pack()

entry_2 = CTkEntry(tela,width = 200, height=30, placeholder_text="Digite aqui",border_color= "#98971a")
entry_2.pack(pady =20)

#frame  de botões
frame_1 = CTkFrame(tela, width = 400, height= 200,fg_color="#282828",border_color="#d65d0e", border_width= 3)
frame_1.pack(padx = 40, pady = 20)
frame_1.pack_propagate()

#Função botões 

#

#função exibir fluxo

#Botões no frame_1
botao_1 = CTkButton(frame_1, width= 80, height= 30, text="+", fg_color="#458588", hover_color= "#076678", command= lambda: Calcular("adição"))
botao_1.configure(font = (None,20,"bold"))
botao_1.grid(row = 0, column = 0, padx=20, pady=20)

botao_2 = CTkButton(frame_1, width= 80, height= 30, text="-", fg_color="#458588", hover_color= "#076678", command= lambda: Calcular("subtração"))
botao_2.configure(font = (None,20,"bold"))
botao_2.grid(row = 0, column = 1, padx=20, pady=20)

botao_3 = CTkButton(frame_1, width= 80, height= 30, text="*", fg_color="#458588", hover_color= "#076678", command= lambda: Calcular("multiplicação"))
botao_3.configure(font = (None,20,"bold"))
botao_3.grid(row = 1, column = 0, padx=20, pady=20)

botao_4 = CTkButton(frame_1, width= 80, height= 30, text="/", fg_color="#458588", hover_color= "#076678", command= lambda: Calcular("divisão"))
botao_4.configure(font = (None,20,"bold"))
botao_4.grid(row = 1, column = 1, padx=20, pady=20)

#resultado
label_2 = CTkLabel(
    tela,
    text="***",
    text_color="#ebdbb2",
    font=("Arial",40),
    anchor="center"
)
label_2.pack()

#Loop
tela.mainloop()