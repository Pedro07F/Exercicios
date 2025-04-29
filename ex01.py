import random

n = random.randint(1,10)
tentativas = 0
u = int(input("Digite um número:"))

while u != n:
    tentativas += 1
    if u < n:
        print("Errou! O número secreto é MAIOR.")
    else:
        print("Errou! O número secreto é MENOR.")

    u = int(input("Digite um número:"))

tentativas += 1
print("Você acertou")
print(f"o numero de tentativas foi {tentativas}")