from collections import Counter
from math import sqrt

def primo(x):
    raiz = int(sqrt(x));

    for i in(3, raiz, 2):
        if (x % i == 0):
            return False;
    else:
        return True;


qt = int(input())

lista = []
listaResposta = []
qtResposta = 0
for _ in range(0, qt):
    lista.append(int(input()))
lista = [key for key, value in Counter(lista).most_common()]
lista.sort()
for n in lista:
    if primo(n):
        qtResposta += 1
        listaResposta.append(n)
ans = '{}\n{}'.format(qtResposta, str(listaResposta).strip('[]'))
if qtResposta > 0:
    ans += '.'
print(ans)
