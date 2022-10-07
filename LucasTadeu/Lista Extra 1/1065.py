# https://www.beecrowd.com.br/judge/pt/problems/view/1065

numero = []
for i in range(5):
    n = int(input())
    numero.append(int(n))

l = 0
for j in range(5):
    if numero[j] % 2 == 0:
        l += 1
print(l, "valores pares")