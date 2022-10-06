# https://www.beecrowd.com.br/judge/pt/problems/view/1009

nome = input()
salarioF = float(input())
vendasM = float(input())

bonus = vendasM * 0.15
final = salarioF + bonus

print("TOTAL = R$ %.2f" %(final))
