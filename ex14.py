numeroContaCliente = int(input("Digite o numero da conta R$: "))
saldoContaCliente = float(input("Digite o saldo da sua conta R$: "))
debitoCliente = float(input("Digite um valor para depositar R$: "))
creditoCliente = float(input("Digite um valor para sacar R$: "))

saldoAtual = saldoContaCliente + debitoCliente - creditoCliente

if saldoAtual >=0.00:
    print("Saldo positivo.")
else:
    print("Saldo negativo.")
    
    