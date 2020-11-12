n = int(input())
k = int(input())

pontuacoes = []

for _ in range(n):
    pontuacoes.append(int(input()))

pontuacoes.sort(reverse=True)

u = pontuacoes[k]
qtd = 0

for i in pontuacoes:
    if i >= i >= u:
        qtd += 1
    else:
        break

print(qtd)
