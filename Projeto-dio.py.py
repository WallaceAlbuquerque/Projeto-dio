nome = str(input("Digite o nome do seu héroi: "))
nivel = eval(input("Digite seu nível: "))

if nivel <= 1000:
    elemento = "Ferro"
elif nivel <= 2000:
    elemento = "Bronze"
elif nivel <= 5000:
    elemento = "Prata"
elif nivel <= 7000:
    elemento = "Ouro"
elif nivel <= 8000:
    elemento = "Platina"
elif nivel <= 9000:
    elemento = "Ascendente"
elif nivel <= 10000:
    elemento = "Imortal"
else:
    elemento = "Radiante"

print(f"O herói de nome {nome} está no nível {elemento}")
