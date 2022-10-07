#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

numero = int(input())

final=1
count=1

while count <= numero:
    final *= count
    count += 1

print("%i! = %i"%(numero,final)) 