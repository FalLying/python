pontos = int(input())

agrupamento_2 = pontos * (pontos - 1) / 2
agrupamento_4 = pontos * (pontos - 1) * (pontos - 2) * (pontos - 3) / 24

r = 1 + agrupamento_2 + agrupamento_4

print(int(r))
