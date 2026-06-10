from customtkinter import *
import time

app = CTk()
app.geometry("1600x900")
app.title("Fluxo de dados e Cálculo")

# Variável global para armazenar a operação selecionada
operacao_selecionada = "+"

# --- ÁREA DEDICADA ÀS FUNÇÕES ---

def selecionar_operacao(op):
    """Define qual operação matemática foi escolhida pelos botões."""
    global operacao_selecionada
    operacao_selecionada = op
    # Feedback visual simples: altera a cor do botão igual para destacar a escolha
    button5.configure(text=f"= ({op})")

def calcular_e_mostrar_fluxo():
    """Esconde a calculadora e mostra o fluxo de dados na CPU."""
    # 1. Pegar os dados das entradas
    num1 = entry_1.get()
    num2 = entry_2.get()
    
    # Validação simples
    if not num1 or not num2:
        num1, num2 = "0", "0"
        
    try:
        # Realiza o cálculo baseado na operação
        n1, n2 = float(num1), float(num2)
        if operacao_selecionada == "+": resultado = n1 + n2
        elif operacao_selecionada == "-": resultado = n1 - n2
        elif operacao_selecionada == "x": resultado = n1 * n2
        elif operacao_selecionada == "÷": resultado = n1 / n2 if n2 != 0 else "Erro (Divisão por 0)"
    except ValueError:
        resultado = "Erro (Dados inválidos)"

    # 2. Dar o .pack_forget() no frame principal da calculadora
    frame_1.pack_forget()
    
    # 3. Criar e exibir o Frame do Fluxo de Dados
    frame_fluxo = CTkFrame(app, width=1600, height=900, fg_color="#121212")
    frame_fluxo.pack(fill="both", expand=True)
    
    # Título da nova tela
    titulo = CTkLabel(frame_fluxo, text="Fluxo de Dados e Processamento", font=("arial", 30, "bold"), text_color="#47A00C")
    titulo.pack(pady=40)
    
    # Container para o diagrama do fluxo
    container_fluxo = CTkFrame(frame_fluxo, fg_color="transparent")
    container_fluxo.pack(pady=20, fill="x", padx=100)
    container_fluxo.columnconfigure((0, 1, 2, 3, 4), weight=1)
    
    # Bloco 1: Entrada de Dados (Teclado/User)
    b_entrada = CTkFrame(container_fluxo, fg_color="#222222", width=250, height=200, corner_radius=15)
    b_entrada.grid(row=0, column=0, padx=10)
    b_entrada.pack_propagate(False)
    CTkLabel(b_entrada, text="1. Entrada (RAM)", font=("arial", 18, "bold"), text_color="#FFF").pack(pady=10)
    CTkLabel(b_entrada, text=f"Reg_A: {num1}\nReg_B: {num2}\nOp: '{operacao_selecionada}'", font=("arial", 16), text_color="#AAA").pack(pady=20)
    
    # Seta 1
    CTkLabel(container_fluxo, text="➔", font=("arial", 40), text_color="#47A00C").grid(row=0, column=1)
    
    # Bloco 2: Processamento (CPU / ULA)
    b_cpu = CTkFrame(container_fluxo, fg_color="#2a2a2a", width=250, height=200, corner_radius=15, border_width=2, border_color="#47A00C")
    b_cpu.grid(row=0, column=2, padx=10)
    b_cpu.pack_propagate(False)
    CTkLabel(b_cpu, text="2. CPU (ULA)", font=("arial", 18, "bold"), text_color="#47A00C").pack(pady=10)
    CTkLabel(b_cpu, text=f"Executando:\n{num1} {operacao_selecionada} {num2}", font=("arial", 16), text_color="#FFF").pack(pady=20)
    
    # Seta 2
    CTkLabel(container_fluxo, text="➔", font=("arial", 40), text_color="#47A00C").grid(row=0, column=3)
    
    # Bloco 3: Saída (Monitor/Display)
    b_saida = CTkFrame(container_fluxo, fg_color="#222222", width=250, height=200, corner_radius=15)
    b_saida.grid(row=0, column=4, padx=10)
    b_saida.pack_propagate(False)
    CTkLabel(b_saida, text="3. Saída (Display)", font=("arial", 18, "bold"), text_color="#FFF").pack(pady=10)
    CTkLabel(b_saida, text=f"Resultado:\n{resultado}", font=("arial", 22, "bold"), text_color="#5CC913").pack(pady=20)

    # Explicação textual abaixo do diagrama
    texto_explicativo = (
        f"O que aconteceu por trás dos panos?\n\n"
        f"1. Os dados inseridos ({num1} e {num2}) foram enviados para a memória RAM e alocados nos registradores.\n"
        f"2. A Unidade de Controle buscou a instrução de '{operacao_selecionada}' e acionou a ULA (Unidade Lógica e Aritmética).\n"
        f"3. A CPU realizou o cálculo binário no circuito somador/subtrator.\n"
        f"4. O resultado final ({resultado}) foi enviado para o buffer de vídeo e renderizado na sua tela."
    )
    
    lbl_explica = CTkLabel(frame_fluxo, text=texto_explicativo, font=("arial", 18), justify="left", text_color="#CCCCCC")
    lbl_explica.pack(pady=50)

    # Botão para voltar para a calculadora
    def voltar():
        frame_fluxo.pack_forget()
        frame_1.pack(fill="both", expand=True)

    btn_voltar = CTkButton(frame_fluxo, text="Voltar para Calculadora", font=("arial", 18), fg_color="#181818", hover_color="#252525", command=voltar)
    btn_voltar.pack(pady=20)


# --- CONFIGURAÇÃO DA INTERFACE ORIGINAL ---

# Frame da calculadora
frame_1 = CTkFrame(app, width=1600, height=900, fg_color="transparent")
frame_1.pack(fill="both", expand=True)

# Configura os frames para dividir igualmente o tamanho do grid
frame_1.grid_columnconfigure(0, weight=1)
frame_1.grid_columnconfigure(1, weight=1)

# Frame do entry
frame_entradas = CTkFrame(frame_1, fg_color="transparent", width=375, height=100)
frame_entradas.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

# Segundo frame para botões
frame_2 = CTkFrame(frame_1, fg_color="transparent", width=400, height=400)
frame_2.grid(row=1, column=0, pady=10, padx=(20, 10), sticky="e")
# Nota: Removido frame_2.pack_propagate(False) pois ele está usando .grid() e causava conflito de layout interno.

# Terceiro frame de botões
frame_3 = CTkFrame(frame_1, fg_color="transparent", width=375, height=400)
frame_3.grid(row=1, column=1, pady=10, padx=(10, 20), sticky="w")

# Entradas 1 e 2
entry_1 = CTkEntry(frame_entradas, width=750, height=50, placeholder_text="Primeiro número", font=("arial", 20))
entry_1.grid(row=0, column=0, pady=10)

entry_2 = CTkEntry(frame_entradas, width=750, height=50, placeholder_text="Segundo número", font=("arial", 20))
entry_2.grid(row=1, column=0)

# Botões de cálculo (Adicionado o parâmetro 'command' apontando para a escolha da operação)
button = CTkButton(frame_2, text="-", text_color="#FFFFFF", fg_color="#181818", font=("arial", 60, "bold"),
                   width=175, height=175, corner_radius=25, hover_color="#141414", command=lambda: selecionar_operacao("-"))
button.grid(row=0, column=0, pady=(0, 10), padx=(0, 10))

button2 = CTkButton(frame_2, text="x", text_color="#FFFFFF", fg_color="#181818", font=("arial", 60, "bold"),
                    width=175, height=175, corner_radius=25, hover_color="#141414", command=lambda: selecionar_operacao("x"))
button2.grid(row=0, column=1, pady=(0, 10), padx=(10, 0))

button3 = CTkButton(frame_2, text="÷", text_color="#FFFFFF", fg_color="#181818", font=("arial", 60, "bold"),
                    width=175, height=175, corner_radius=25, hover_color="#141414", command=lambda: selecionar_operacao("÷"))
button3.grid(row=1, column=0, pady=(10, 0), padx=(0, 10))

button4 = CTkButton(frame_2, text="+", text_color="#FFFFFF", fg_color="#181818", font=("arial", 60, "bold"),
                    width=175, height=175, corner_radius=25, hover_color="#141414", command=lambda: selecionar_operacao("+"))
button4.grid(row=1, column=1, pady=(10, 0), padx=(10, 0))

# Botão de Igual (Adicionado o 'command' para chamar a função do fluxo de dados)
button5 = CTkButton(
    frame_3,
    text="=",
    text_color="#FFFFFF",
    fg_color="#47A00C",
    font=("arial", 60, "bold"),
    width=350,
    height=360,
    corner_radius=100,
    hover_color="#5CC913",
    command=calcular_e_mostrar_fluxo
)
button5.pack()

app.mainloop()