def calculoSalario(salarioAtual, percentual):
    salarioReajustado = salarioAtual * (percentual/100)
    novoSalario = salarioAtual + salarioReajustado
    return salarioReajustado, novoSalario

nomeColaborador = str(input("Digite o nome do colaborador: "))
salarioColaborador = float(input("Digite o salario mensal do colaborador: "))

if salarioColaborador <= 280.00:
    percentual = 20
elif salarioColaborador <= 700.00: 
    percentual = 15
elif salarioColaborador <= 1.500:
    percentual = 10
else:
    percentual = 5
    
salarioAdicionado,valorFinal = calculoSalario(salarioColaborador, percentual)

resultado = (f'''
Nome do colaborador: {nomeColaborador}
Salario mensal: R${salarioColaborador:.2f}
Percentual do aumento: {percentual}
Salario adicionado com base no percentual: {salarioAdicionado:.2f}
Salario atualizado com aumento do percentual: {valorFinal:.2f}
''')

print(resultado)