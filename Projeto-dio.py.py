nome = str(input("Digite o nome do seu héroi: "))
nivel = eval(input("Digite seu nível: "))

if nivel <= 1000:
    print("Ferro")
elif nivel > 1001 and nivel <= 2000:
    print("Bronze")
elif nivel > 2001 and nivel <= 5000:
    print("Prata")
elif nivel > 5001 and nivel <= 7000:
    print("Ouro")
elif nivel > 7001 and nivel <= 8000:
    print("Platina")
elif nivel > 8001 and nivel <= 9000:
    print("Ascendente")
elif nivel > 9001 and nivel <= 10000:
    print("Imortal")
else:
    print("Radiante")
    
print(f"O héroi de nome {nome} está no nível", + nivel)