nomecolaborador = str(input("Digite o nome do colaborador: "))
valorHora = float(input("Digite o valor que ganha por hora: "))
horaTrabalhadaMes = int(input("Digite a quantidade de horas trabalhadas no mes:"))
salarioBruto = valorHora * horaTrabalhadaMes

if salarioBruto <= 900:
    print("Seu salario liquido mensal eh de:{} ".format(salarioBruto))
elif salarioBruto <= 1500:
    percentualmposto = 5
elif salarioBruto <= 2500:
    percentualmposto = 10
else:
    percentualmposto = 20
    
    
totalValorImposto = salarioBruto * (percentualmposto/100) #Cálculo do Imposto de Renda
totalSindicato = salarioBruto * 0.03 #3% do Sindicato
totalFGTS = salarioBruto * 0.11 #11% do Salário Bruto
totalDescontos = totalValorImposto + totalSindicato #Valor total descontado do salário
salarioLiquido = salarioBruto - totalDescontos #Salário Liquido

print('\n')
print("==============================================================================")
print(f'Segue abaixo as informações sobre o salário do colaborador {nomecolaborador}:')
print(f'- Salario bruto: R${salarioBruto:.2f}')
print(f'- Imposto de Renda de {percentualmposto}% aplicados: R${totalValorImposto:.2f}')
print(f'- Aplicado percentual de 3% do Sindicato: R${totalSindicato:.2f}')
print(f'- Aplicado percentual de 11% do FGTS: R${totalFGTS:.2f}')
print(f'- Total de descontos: R${totalDescontos:.2f}')
print(f'- Salario Liquido: {salarioLiquido:.2f}')