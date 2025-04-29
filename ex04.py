soma = 0
n = int(input("Digite um número:"))

while n != 0:
    soma += n
    print(f"Soma até agora: {soma}")
    n = int(input("Digite um número:"))

print("Você chegou ao fim do desafio")
print("A soma total dos números é:", soma)