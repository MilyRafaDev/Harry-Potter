print('*Bem-vindo ao Chapéu Seletor!*')
print('Responda às perguntas abaixo com sinceridade, e indicaremos sua casa de Hogwarts.')

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
        "pergunta": "Você é mais?...",
        "opcoes": {
            'A': ("Determinado(a)", "Grifinoria"),
            'B': ("Astuto(a)", "Sonserina"),
            'C': ("Criativo(a)", "Corvinal"),
            'D': ("Trabalhador(a)", "Lufa-Lufa")
        }
    },
    {
        "pergunta": "O que você mais admira em um bruxo?",
        "opcoes": {
            'A': ("Sua Lealdade", "Grifinoria"),
            'B': ("Sua Justiça", "Lufa-Lufa"),
            'C': ("Sua Determinação", "Sonserina"),
            'D': ("Sua Curiosidade", "Corvinal")
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

for q in perguntas:
    print('\n' + q["pergunta"])
    for letra, (resposta, _) in q["opcoes"].items():
        print(f"{letra}) {resposta}")

    escolha = input("Sua resposta: ").upper()

    while escolha not in q["opcoes"]:
        escolha = input("Escolha inválida. Tente novamente (A, B, C, D): ").upper()

    casa_escolhida = q["opcoes"][escolha][1]
    casas[casa_escolhida] += 1

casa_final = max(casas, key=casas.get)

print(f"\nParabéns! O Chapéu Seletor decidiu: você pertence à casa **{casa_final}**!")
