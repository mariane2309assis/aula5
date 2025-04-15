x = 0
media=0
qntd = int(input("quants alunos tem na sala"))
while x < qntd:
        valor = int(input("digite as notas: "))
        media+=valor
        x += 1
media= media/qntd
print("a média da turma é:", media)