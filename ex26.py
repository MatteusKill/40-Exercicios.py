valorAquisição = float(input("Digite o valor da aquisição do produto (R$): "))

if valorAquisição < 50.00:
    valorVenda = valorAquisição * 1.45
    print(f'\nAplicando lucro de 45%.')
else:
    valorVenda = valorAquisição * 1.30
    print('\nAplicando lucro de 30%.')
    
print(f'O valor de venda do produto eh: R${valorVenda:.2f}')