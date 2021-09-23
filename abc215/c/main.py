from itertools import permutations
s, k = input().split()
k = int(k)
ans = set()

for i in permutations(list(s), len(s)):
    ans.add(''.join(i))
ans = sorted(ans)
print(ans[k-1])
