soma = 0

for i in range(1, 5):
    nota = float(input(f"Digite a {i}ª nota: "))
    soma += nota

media = soma / 4

print(f"\nMédia final: {media:.2f}")

if media >= 7:
    print("Status: APROVADO!")
elif media >= 5:
    print("Status: EM RECUPERAÇÃO!")
else:
    print("Status: REPROVADO!")
