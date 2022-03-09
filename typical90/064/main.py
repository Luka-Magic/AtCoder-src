n, q = map(int, input().split())
li = list(map(int, input().split()))

dif = [0] * (n-1)
E = 0
for i in range(n-1):
    dif[i] = li[i+1] - li[i]
    E += abs(dif[i])

for _ in range(q):
    l, r, v = map(int, input().split())
    if l != 1:
        l = l-2
        E += abs(dif[l] + v) - abs(dif[l])
        dif[l] += v
    if r != n:
        r = r-1
        E += abs(dif[r] - v) - abs(dif[r])
        dif[r] -= v
    print(E)