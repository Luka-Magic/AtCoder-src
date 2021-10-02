n = int(input())
li = list(map(int, input().split()))
ans = 10**9+7
for i in li:
    k = 0
    while 1:
        if i % 2 != 0:break
        k += 1
        i //= 2
    ans = min(ans, k)
print(ans)