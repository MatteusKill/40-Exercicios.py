nomeUsuario = str(input("Digite o seu nome: "))
idadeUsuario = int(input("Digite a sua idade: "))

if idadeUsuario <= 2:
    tipo = 'Bebe'
elif idadeUsuario <= 11:
    tipo = 'Crianca'
elif idadeUsuario <=21:
    tipo = 'Jovem'
elif idadeUsuario <= 64:
    tipo = 'Adulto'
elif idadeUsuario <= 100:
    tipo = 'Idoso'
else: 
    tipo = 'Mumia'

print(f"{nomeUsuario} tem {idadeUsuario} e eh considerado {tipo}.")