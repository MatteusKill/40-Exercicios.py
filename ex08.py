distancia = float(input("Digite a distancia total da viagem em km: "))
consumoMedio = float(input("Digite o consumo médio do carro km/litro:"))
precoCombustivel = float(input("Digite o preço do litro do combustivel em reais: "))

litrosNecessarios = distancia / consumoMedio

custoTotal = litrosNecessarios * precoCombustivel

print(f"Distância da Viagem: {distancia} km")
print(f"Consumo do Veículo: {consumoMedio} km/l")

print(f"Litros de combustível necessários: {litrosNecessarios:.2f} L")
print(f"O custo estimado apenas com combutível será de: R$ {custoTotal:.2f}")