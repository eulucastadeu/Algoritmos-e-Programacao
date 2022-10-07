# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761

soma = 0
valor = 1
while valor != 0:
    valor = float(input())
    soma = soma + valor

pagamento = float(input())
print("Total da compra: R$%.2f"%(soma))
print("Valor pago: R$%.2f"%(pagamento))
print("Troco: R$%.2f"%(pagamento - soma))
    