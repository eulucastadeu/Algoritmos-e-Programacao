# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

valorProduto = float(input())

lucro1 = valorProduto * 0.45
lucro2 = valorProduto * 0.3

if valorProduto < 20:
    print("Valor de venda: R$ %.2f" %(valorProduto + lucro1))
else:
    print("Valor de venda: R$ %.2f" %(valorProduto + lucro2))  