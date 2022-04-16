n = int(input())
li = list(map(lambda x:bin(int(x))[2:].zfill(61), input().split()))

ans = 0

mod = 10**9 + 7

for i in range(61):
    n0 = 0
    n1 = 0
    for l in li:
        if l[61 - i - 1] == '1':
            n1 += 1
        else:
            n0 += 1
    ans += (((n0 * n1) % mod) * (pow(2, i, mod))) % mod
    ans %= mod

print(ans)

