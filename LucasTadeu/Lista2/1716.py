# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

codigo = input()
salario = float(input())

if codigo == "A":
    print("Novo salário: R$%.2f"%(salario + (salario * 0.1))) 

if codigo == "B":
    print("Novo salário: R$%.2f"%(salario + (salario * 0.15))) 

elif codigo == "C":
    print("Novo salário: R$%.2f"%(salario + (salario * 0.2))) 
