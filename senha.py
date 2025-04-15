pin=1234
tentativa =1
msg= "senha bloqueada"
while tentativa <=3:
    senha=int(input("digite a senha: "))
    if senha ==pin:
        msg="senha correta"
        print("senha correta!")
        break
    tentativa+=1
print(msg)