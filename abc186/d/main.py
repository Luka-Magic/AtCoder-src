n = int(input())
li = list(map(int, input().split()))
li.sort()
ans = 0
for i, k in enumerate(li):
    ans += k * (2 * i - n + 1)
print(ans)
