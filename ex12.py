numeroDigitado = float(input("Digite um numero para saber se eh negativo ou positivo: "))

if numeroDigitado < 0.00: 
    print("O numero eh negativo.")
elif numeroDigitado == 0.00:
    print("O numero eh 0.")
else:
    print("O numero eh positivo.")