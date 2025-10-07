nomeAluno = str(input("Digite o nome do aluno: "))
nomeDisciplina = str(input("Digite o nome da disciplina: "))
notaP1 = float(input("Digite a nota da prova 01: "))
notaP2 = float(input("Digite a nota da prova 02: "))
notaP3 = float(input("Digite a nota da prova 03: "))

media = (notaP1 + notaP2 + notaP3) /3

if media >= 6.0: 
    print(f"O aluno {nomeAluno} foi aprovado!")
else:
    print(f"O aluno {nomeAluno} foi reprovado!")
    
