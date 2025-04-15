resp = "s"
while resp == "s":
    nota1 = float(input("digite a nota 1"))
    while nota1 < 0 or nota1 > 10:
            nota1 = float(input("digite a nota 1"))
    nota2 = float(input("digite a nota 2"))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("digite a nota 2"))
    media= (nota1+nota2)/2
    print(media)
    resp= input(" deseja fazer o calculo novamente (s/n)")