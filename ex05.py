nomeAluno = str(input("Digite o nome do aluno: "))
nomeDisciplina = str(input("Digite o nome da disciplina: "))
notaP1 = float(input("Digite a nota da prova 01: "))
notaP2 = float(input("Digite a nota da prova 02: "))
notaP3 = float(input("Digite a nota da prova 03: "))

media = (notaP1 + notaP2 + notaP3) /3

print(f"Nome do aluno: {nomeAluno}")
print(f"Nome da disciplina: {nomeDisciplina}")
print(f"Nota prova 01: {notaP1}")
print(f"Nota prova 02: {notaP2}")
print(f"Nota prova 03: {notaP3}")

print(f"A media como base nas notas atingidas eh: {media}")
 