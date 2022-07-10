n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

from itertools import permutations
for i, m in enumerate(permutations(list(range(1, n+1)), n)):
    if m == p:
        a = i
    if m == q:
        b = i

print(abs(a - b))