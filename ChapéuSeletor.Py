from tkinter import *

# ------------------------------
# Cores
# ------------------------------
Branco = "#ffffff"
Preto = "#000000"
Vermelho = "#a6332e"
Amarelo = "#efbc2f"
Azul = "#3c4e91"
Verde = "#366447"
pergaminho = "#e9cba5"

# ------------------------------
# Dados do Chapéu Seletor
# ------------------------------

casas = {
    "Grifinoria": 0,
    "Sonserina": 0,
    "Lufa-Lufa": 0,
    "Corvinal": 0
}

perguntas = [
    {
        "pergunta": "Qual dos atributos abaixo você mais valoriza?",
        "opcoes": {
            'A': ("Inteligência", "Corvinal"),
            'B': ("Ambição", "Sonserina"),
            'C': ("Lealdade", "Lufa-Lufa"),
            'D': ("Coragem", "Grifinoria")
        }
    },
    {
        "pergunta": "Com qual animal você mais se identifica? ",
        "opcoes": {
            'A': ("Leão", "Grifinoria"),
            'B': ("Cobra", "Sonserina"),
            'C': ("Aguia", "Corvinal"),
            'D': ("Texugo", "Lufa-Lufa")
        }
    },
    {
        "pergunta": "Você se definiria como?...",
        "opcoes": {
            'A': ("Impulsivo(a)", "Grifinoria"),
            'B': ("Paciente", "Lufa-Lufa"),
            'C': ("Persistente", "Sonserina"),
            'D': ("Independente", "Corvinal")
        }
    }
]

# ------------------------------
# Variáveis de controle
# ------------------------------

indice_pergunta = 0

# ------------------------------
# Funções
# ------------------------------

def mostrar_pergunta():
    global indice_pergunta
    if indice_pergunta < len(perguntas):
        pergunta_atual = perguntas[indice_pergunta]
        texto_pergunta.config(text=pergunta_atual["pergunta"])

        botao_A.config(text=f"A) {pergunta_atual['opcoes']['A'][0]}")
        botao_B.config(text=f"B) {pergunta_atual['opcoes']['B'][0]}")
        botao_C.config(text=f"C) {pergunta_atual['opcoes']['C'][0]}")
        botao_D.config(text=f"D) {pergunta_atual['opcoes']['D'][0]}")

    else:
        mostrar_resultado()

def responder(letra):
    global indice_pergunta

    pergunta_atual = perguntas[indice_pergunta]
    casa_escolhida = pergunta_atual["opcoes"][letra][1]
    casas[casa_escolhida] += 1

    indice_pergunta += 1
    mostrar_pergunta()

def mostrar_resultado():
    casa_final = max(casas, key=casas.get)
    texto_pergunta.config(text=f"Parabéns! O Chapéu Seletor decidiu: você pertence à casa {casa_final}!")

    frame_botoes.pack_forget()

# ------------------------------
# Interface Gráfica
# ------------------------------

janela = Tk()
janela.title("Chapéu Seletor")
janela.geometry("484x384")
janela.configure(bg=Preto)

texto_pergunta = Label(janela, text="", font=("Georgia", 20), wraplength=450, height=2, width=500, bg=Branco)
texto_pergunta.pack(pady=1, padx=1)

# Frame para os botões
frame_botoes = Frame(janela, bg=Preto)
frame_botoes.pack()

botao_A = Button(frame_botoes, text="", bg=Vermelho, fg=Branco, width=21, height=6, font=("Georgia 14"),
                 command=lambda: responder('A'))
botao_A.grid(row=0, column=0, padx=1, pady=1)

botao_B = Button(frame_botoes, text="", bg=Amarelo, fg=Branco, width=21, height=6, font=("Georgia 14"),
                 command=lambda: responder('B'))
botao_B.grid(row=0, column=1, padx=1, pady=1)

botao_C = Button(frame_botoes, text="", bg=Azul, fg=Branco, width=21, height=6, font=("Georgia 14"),
                 command=lambda: responder('C'))
botao_C.grid(row=1, column=0, padx=1, pady=1)

botao_D = Button(frame_botoes, text="", bg=Verde, fg=Branco, width=21, height=6, font=("Georgia 14"),
                 command=lambda: responder('D'))
botao_D.grid(row=1, column=1, padx=1, pady=1)

mostrar_pergunta()

janela.mainloop()
