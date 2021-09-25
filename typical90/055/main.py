from itertools import combinations
n, p, q = map(int, input().split())
li = list(map(int, input().split()))
ans = 0
for a, b, c, d, e in combinations(li, 5):
    if a*b*c*d*e % p == q:
        ans += 1
print(ans)
