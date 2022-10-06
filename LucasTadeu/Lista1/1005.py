# https://www.beecrowd.com.br/judge/pt/problems/view/1005

A = float(input())
B = float(input())
peso1 = 3.5
peso2 = 7.5
media = (A*peso1 + B*peso2)/(peso1+peso2)

if A > 10 or B > 10:
    print("Erro, nota maior que 10")
else:
    print("MEDIA = %.5f" %(media)) 