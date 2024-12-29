rows = 9
for i in range(0, rows + 1):
    # Adiciona espaços no início de cada linha para inverter a direção
    for space in range(i):
        print(" ", end=" ")
    # Imprime os números
    for j in range(1, rows - i + 1):
        print("*", end=" ")
    print()
input()
