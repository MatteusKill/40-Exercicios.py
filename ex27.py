numeroMatricula = int(input("Digite o numero da matricula: "))
sexoAluno = (input("Digite o seu sexo em 'M' ou 'F': ")) .lower()
alturaAluno = float(input("Digite a sua altura: "))
fisicoAluno = int(input("Digite o status do seu fisico em '1- Bom' '2- Regular' '3- Ruim': "))

contadorFemininoAlto = 0
contadorMasculino = 0


if sexoAluno == 'F' and alturaAluno > 1.70:
    contadorFemininoAlto = +1
    
if sexoAluno == 'M' and fisicoAluno == 1:
    contadorMasculino = +1
    
print(f'A quantidade de alunos do sexo femino com altura maior que 1.70M eh: {contadorFemininoAlto}')
print(f'A quantidade alunos do sexo Masculino cujo status fisico bom eh: {contadorMasculino}')