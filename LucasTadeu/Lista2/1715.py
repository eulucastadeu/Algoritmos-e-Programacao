# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

codigo = int(input())
valor = float(input())

if codigo == 1:
    print("Valor total a ser pago: R$%.2f"%(valor))

elif codigo == 2:
    funcionario = valor * 0.13
    final = valor - funcionario
    print("Valor total a ser pago: R$%.2f"%(final))

elif codigo == 3:
    clientePremium = valor * 0.07
    final2 = valor - clientePremium
    print("Valor total a ser pago: R$%.2f"%(final2))

else:
    print("OPÇÃO INVÁLIDA!") 