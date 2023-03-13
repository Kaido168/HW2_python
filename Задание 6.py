n = int(input())
f = 1
ans = 1
for i in range(1, n + 1):
    f *= i
    ans += 1/f
print(ans)
