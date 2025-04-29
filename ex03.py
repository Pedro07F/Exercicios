usuario = int(input("Qual o numero?"))
chances = 0

while chances <=2 :
    if usuario == 0:
        print("Você acertou!")
        break
    else:
        print("Número incorreto!")
        chances += 1
        if chances < 3:
            usuario = int(input("Tente novamente: "))

print('Limites de chances alcançada')