import bisect

n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

ans = 0
for i in t:
    k = bisect.bisect_left(s, i)
    if k == n or s[k] != i:
        continue
    ans += 1

print(ans)