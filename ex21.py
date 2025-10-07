porcentagemComissao = 0.04

salarioFixo = float(input('Digite o valor do salário fixo: R$ '))
valorVendas = float(input('Digite o valor total de vendas: R$ '))

valorComissao = valorVendas * porcentagemComissao

salarioFinal = salarioFixo + valorComissao

print(f'Valor da comissão: R$ {valorComissao:.2f}')
print(f'Salário final: R$ {salarioFinal:.2f}')