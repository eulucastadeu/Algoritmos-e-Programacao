# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

recebe_p_horas = float(input())
horas = float(input())

salario = recebe_p_horas * horas

imposto = salario*0.11
inss = salario*0.08
sindicato = salario*0.05

desconto = imposto + inss + sindicato

print("Salário bruto: R$%.2f" %(salario)) 
print("Imposto: R$%.2f" %(imposto))
print("INSS: R$%.2f" %(inss))
print("Sindicato: R$%.2f" %(sindicato)) 
print("Líquido: R$%.2f" %(salario - desconto)) 