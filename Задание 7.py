vvod = int(input())
schet = 0
for i in range(1, vvod):
    if vvod % i != 0: continue
    else: schet = schet + 1
print(schet +1)

