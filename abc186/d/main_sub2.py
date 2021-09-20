n = int(input())
li = list(map(int, input().split()))
s = sum(li)
t = 0
ans = 0
li.sort()
for i in range(n):
    ans += s - t - li[i]*(n-i)
    t += li[i]
print(ans)
