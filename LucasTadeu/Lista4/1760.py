# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

numero = 0
soma = 0
contador = 0

for numero in range(4):
    idade = int(input())
    soma = soma + idade

    peso = float(input()) 

    if peso > 90:
        contador = contador + 1

print("Qtd pessoas > 90 Kg: %i"%(contador)) 
media = soma/4
print("Idade média: %.2f"%(media)) 

