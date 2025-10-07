porcentagemDesconto = 0.10

precoOriginal = float(input('Digite o preco do produto: R$ '))

valorDesconto = precoOriginal * porcentagemDesconto
novoPreco = precoOriginal - valorDesconto

print(f'Preço original: R$ {precoOriginal:.2f}')
print(f'Valor do desconto: R$ {valorDesconto:.2f}')
print(f'Novo preço com desconto: R$ {novoPreco:.2f}')