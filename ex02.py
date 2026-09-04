partidas = (
    ("Ana", 10),
    ("Bruno", 7),
    ("Carlos", 8),
    ("Ana", 5),
    ("Bruno", 10),
    ("Carlos", 4),
    ("Ana", -2)
)

'''pontos = {}

for jogador, valor in partidas:
    if jogador not in pontos:
        pontos[jogador] = 0

    pontos[jogador] += valor

campeao = ""

for jogador in pontos:
    campeao = jogador

print(campeao)'''

'''pontos = {}

for jogador, valor in partidas:
    if jogador not in pontos:
        pontos[jogador] = 0

campeao = ""
maior_pontuacao = None

for jogador in pontos:
    if maior_pontuacao is None or pontos[jogador] > maior_pontuacao:
        maior_pontuacao = pontos[jogador]
        campeao = jogador

    print(campeao)'''


'''pontos = {}

for jogador, valor in partidas:
    if jogador not in pontos:
        pontos[jogador] = valor
    else:
        pontos[jogador] = pontos[jogador] + valor

campeao = ""
maior_pontuacao = 0

for jogador in pontos:
    if pontos[jogador] >= maior_pontuacao:
        maior_pontuacao = pontos[jogador]
        campeao = jogador

        print(campeao)'''


pontos = {}

for jogador, valor in partidas:
    pontos[jogador] = valor

campeao = ""

for jogador in pontos:
    if pontos[jogador] > pontos[campeao]:
        campeao = jogador
print(campeao)