nome = input()
horas_extras = float(input())

salario_minimo = 1192.40
valor_horaExtra = 10.00
#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

salario_horaExtra = horas_extras * valor_horaExtra
salarioBruto = 3 * salario_minimo + salario_horaExtra

if salarioBruto > 2000.00:
    inss = salarioBruto*0.12
     
else:
    inss = salarioBruto*0.05

#Imposto

if salarioBruto > 2500.00:
    imposto = salarioBruto * 0.2 

descontos = inss + imposto

salarioLiquido = salarioBruto - descontos

print("Nome: %s" %(nome))
print("Salário bruto: R$%.2f"%(salarioBruto))
print("Salário Líquido: R$%.2f"%(salarioLiquido)) 