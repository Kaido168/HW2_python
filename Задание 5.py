H = 0
G = int (input())
J = 1
K = -1
while G != 0:
        F = max(G , H)
        G = int(input())
        if K == F:
            J = 0
            break
        elif G == F:
                J += 1
print(J)