# Um programa que soma a média de 5 alunos e faça a média aritmética entre eles

somaMedias=0
for i in range(5):
    nota1 = int(input(f"Digite a primeira nota do aluno {i+1}\n"))
    nota2 = int(input(f"Digite a segunda nota do aluno {i+1}\n"))
    nota3 = int(input(f"Digite a terceira nota do aluno {i+1}\n"))
    media = (nota1+nota2+nota3)/3
    somaMedias += media
    mediaGeral = somaMedias/5
print(f"A média aritmética dos 5 alunos é: {mediaGeral}")