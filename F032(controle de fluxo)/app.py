from turtle import Turtle
t = Turtle()

t.speed(1)
while True:
    print("===== Bem-vindo ao jogo da Turtle =====")
    continuar = input("Deseja continuar? (S/N): ").strip().lower()
    if continuar == "n":
        break
    elif continuar == "s":
        escolha = input("Deseja andar para frente, trás, cima ou embaixo? (Fr/Ts/Ci/Ba): ").strip().lower()
        distancia = int(input("Quantos pixels deseja andar? \n"))
        if escolha == "fr":
            t.forward(distancia)
        elif escolha == "ts":
            t.backward(distancia)
        elif escolha == "ci":
            t.left(90)
            t.forward(distancia)
            t.right(90)
        elif escolha == "ba":
            t.right(90)
            t.forward(distancia)
            t.left(90)
        else:
            print("Escolha inválida. Digite 'Fr' para frente, 'Ts' para trás, 'Ci' para cima ou 'Ba' para baixo.")
    else:
        print("Escolha inválida. Digite 'S' para continuar ou 'N' para sair.")
