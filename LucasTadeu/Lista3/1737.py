# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737

qnt = int(input())
soma = 0
cont = 0

if qnt <= 0:
    print("Informe uma quantidade > 0!")

else:
    while cont < qnt:
        numeros = float(input())
        soma = soma + numeros
        cont = cont + 1
    print("Soma dos números informados: %.2f" %(soma)) 