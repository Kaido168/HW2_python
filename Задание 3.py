R = 0
G = -1
P = 0
while G != 0:
    G = int(input())
    P = P + G
    if G != 0:
        R += 1
print(P/R)
