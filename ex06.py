opcao = 0

while opcao != 3:
    print(" [1] Somar dois numeros \n [2] Multiplicar dois numeros \n [3] Sair do programa")
    opcao = int(input("Digite sua opcao: "))

    
    if opcao == 1:
        n1 = int(input("Primeiro numero: "))
        n2 = int(input("Segundo numero: "))
        print("o resultado da operação é", n1+n2)

    elif opcao == 2:
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        print("o resultado da operação é", n1*n2)

    elif opcao == 3:
        print("Saindo do programa...")

    else:
        print("Opção inválida")

print("Programa encerrado!")