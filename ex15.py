letraDigitada = str(input("Digite uma letra para M/F: ")).lower() 
#lower = tudo maiusculo para minusculo; upper = tudo minusculo para maiusculo

if letraDigitada == 'f':
    print("F-Feminino.")
elif letraDigitada == 'm':
    print("M-Masculino.")
else:
    print("Sexo invalido.")
    
    